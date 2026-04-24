from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from dotenv import load_dotenv
from django.shortcuts import render

# LlamaIndex imports
from llama_index.core import Document, SummaryIndex, Settings
from llama_index.llms.groq import Groq

# Charger les variables d'environnement
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configuration de LlamaIndex avec Groq
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
Settings.llm = llm
Settings.embed_model = None  # Pas besoin d'embeddings avec SummaryIndex pour ce volume

# Introduction et Connaissances sur l'AN-ETAT (Bilingue pour aider l'IA)
knowledge_base = [
    # Version Française
    Document(text=(
        "L'Agence Numérique de l’Etat (AN-ETAT) est l'instrument principal de la Mauritanie pour la transformation numérique. "
        "Elle a été créée par le décret 074-2023 du 26 avril 2023. Elle pilote l'Agenda de Transformation Numérique 2022-2025. "
        "Services : e-administration, cybersécurité, infrastructures IT, soutien à l'innovation et aux startups. "
        "Objectifs : Améliorer l'efficacité de l'administration publique et moderniser les secteurs socio-économiques."
    )),
    # Version Anglaise
    Document(text=(
        "The State Digital Agency (AN-ETAT) is Mauritania's primary instrument for digital transformation. "
        "It was created by decree 074-2023 on April 26, 2023. It leads the 2022-2025 Digital Transformation Agenda. "
        "Services: e-administration, cybersecurity, IT infrastructure, support for innovation and startups. "
        "Objectives: Improve public administration efficiency and modernize socio-economic sectors."
    )),
    Document(text="Horaires / Hours: Lundi au vendredi / Monday to Friday, 08h00 - 17h00."),
    Document(text="Contact: Email contact@an-etat.mr, Site web: www.an-etat.mr.")
]

# Initialisation de l'index LlamaIndex
index = SummaryIndex.from_documents(knowledge_base)

# Configuration du System Prompt pour le multilinguisme
SYSTEM_PROMPT = (
    "You are the official AI assistant of the Mauritanian State Digital Agency (AN-ETAT). "
    "Use the provided context to answer questions. "
    "CRITICAL: You must answer EXCLUSIVELY in the language of the user's question. "
    "If asked in English, use the English context. Do not include French words in English answers."
)

query_engine = index.as_query_engine(system_prompt=SYSTEM_PROMPT)

def chatbot_test_view(request):
    return render(request, 'chatbot/chatbot_test.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def chatbot_view(request):
    """
    API du chatbot utilisant LlamaIndex et Groq.
    """
    try:
        data = json.loads(request.body)
        user_question = data.get("question", "").strip()

        if not user_question:
            return JsonResponse({"error": "Veuillez poser une question."}, status=400)

        # Utilisation de LlamaIndex pour générer la réponse
        response = query_engine.query(user_question)
        response_text = str(response)

        return JsonResponse({"response": response_text})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
