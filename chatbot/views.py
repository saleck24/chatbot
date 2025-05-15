from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
from difflib import get_close_matches

# Charger les variables d'environnement
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configurer LlamaIndex avec Groq
llm = Groq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

#Tester le chat avec le front chatbot_test.html
from django.shortcuts import render

def chatbot_test_view(request):
    return render(request, 'chatbot/chatbot_test.html')


# Introduction sur l'AN-ETAT
intro_an_etat = (
    "L'agence Numérique de l’Etat ou AN-ETAT joue un rôle primordial dans la mise en oeuvre des programmes inscrits dans l'Agenda de Transformation Numérique 2022-2025. "
    "Il s’agit de l’instrument principal du ministère en charge du numérique pour la mise en oeuvre des programmes de transformation numérique au service de l’Administration publique et des secteurs socio-économiques. "
    "L’AN-ETAT a été créé conformément au décret 074-2023 du 26 avril 2023. "
    "L'AN-ETAT cherche à renforcer sa légitimité en mettant en place un site Web pour fournir des informations clés sur l'agence, ses activités, ses projets et faciliter la communication avec les parties prenantes."
)

# Liste des questions fréquentes
FAQ = {
    "Quels sont les services proposés par l'AN-ETAT ?": "L'AN-ETAT offre des services numériques comme l'e-administration, la cybersécurité et la gestion des infrastructures IT.",
    "Comment contacter l'AN-ETAT ?": "Vous pouvez contacter l'AN-ETAT via leur site officiel ou par email à contact@an-etat.mr.",
    "Quels sont les horaires d'ouverture ?": "L'AN-ETAT est ouvert du lundi au vendredi de 08h00 à 17h00.",
    "Comment accéder aux services en ligne ?": "Vous pouvez accéder aux services en ligne via le portail officiel de l'AN-ETAT : www.an-etat.mr.",
    "Quels sont les objectifs de l'Agence Numérique de l'État ?": "L'Agence Numérique de l'État vise à piloter la transformation numérique en Mauritanie en mettant en œuvre des projets stratégiques pour améliorer l'efficacité et la productivité.",
    "Comment l'Agence Numérique de l'État facilite-t-elle la numérisation de l'administration ?": "Elle simplifie les procédures gouvernementales et améliore la qualité des services publics grâce à la digitalisation.",
    "Quels secteurs bénéficient du développement des infrastructures numériques ?": "L'éducation la santé et l'économie sont des secteurs clés bénéficiant de la transformation numérique.",
    "Comment l'agence soutient-elle l'innovation et l'entrepreneuriat ?": "Elle encourage les startups et les nouvelles technologies pour dynamiser l'économie numérique.",
    "Quel est le rôle des partenariats dans la transformation numérique ?": "L'agence collabore avec les secteurs public et privé pour assurer une intégration numérique efficace.",
    "Quelle est la vision à long terme de la transformation numérique ?": "La mise en œuvre d'une stratégie nationale durable pour un avenir numérique avancé et aligné sur les tendances mondiales."
}

# Définition du prompt pour le service utilisateur (amélioré pour plus de professionnalisme et de clarté)
response_synthesis_prompt_st = (
    "You are an AI assistant designed to provide professional, precise, and well-structured responses. "
    "Your answers must always be direct, natural, and exclusively in the language of the user's query, whether it's Arabic, French, English, Spanish, or any other language. "
    "Never mention language detection, translation, or switch to another language, or put the query in the answers unless explicitly requested by the user. "
    "If a query is in a specific language, respond in that same language, even if the initial query was in a different language. "
    "If you do not have the answer to a query, search for it on the internet to provide the most accurate and up-to-date information. "
    "Ensure that your responses align perfectly with the following description of the Mauritanian State Digital Agency (AN-ETAT), adapting the content naturally to the user's language and cultural context:\n\n"
    
    "L'Agence Numérique de l'État (AN-ETAT) joue un rôle central dans la mise en œuvre des programmes inscrits dans l'Agenda de Transformation Numérique 2022-2025. "
    "Elle constitue l’outil stratégique du ministère en charge du numérique pour piloter les initiatives de transformation numérique au service de l’Administration publique et des secteurs socio-économiques. "
    "Créée conformément au décret 074-2023 du 26 avril 2023, l’AN-ETAT est chargée d'accompagner l'innovation et de moderniser les services publics grâce à des solutions numériques adaptées."
)



@api_view(['POST'])
@permission_classes([AllowAny])
#@csrf_exempt   Désactiver CSRF pour simplifier les tests
def chatbot_view(request):
    """
    API du chatbot qui répond aux questions des utilisateurs.
    """
    try:
        data = json.loads(request.body)
        user_question = data.get("question", "").strip()

        if not user_question:
            return JsonResponse({"error": "Veuillez poser une question."}, status=400)

        # Vérifier si la question est dans la FAQ
        similar_questions = get_close_matches(user_question, FAQ.keys(), n=1, cutoff=0.7)
        if similar_questions:
            return JsonResponse({"response": FAQ[similar_questions[0]]})

        # Demander une réponse à Groq avec le prompt configuré
        prompt = f"{response_synthesis_prompt_st} La question de l'utilisateur est : {user_question}"
        response = llm.complete(prompt)

        # Si Groq ne donne pas de réponse, fournir la réponse par défaut
        if not response or not response.text.strip():
            response_text = intro_an_etat  # Utilisation de l'introduction de l'AN-ETAT comme réponse par défaut
        else:
            response_text = response.text

        return JsonResponse({"response": response_text})


    except json.JSONDecodeError:
        return JsonResponse({"error": "Requête invalide. Assurez-vous d'envoyer des données JSON."}, status=400)
