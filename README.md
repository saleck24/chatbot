# 🤖 Chatbot IA Intelligent - AN-ETAT

## 🌟 Aperçu
Un **chatbot intelligent basé sur l'IA** conçu pour l'Agence Numérique de l'État (AN-ETAT) en Mauritanie. Ce système combine des technologies de pointe en traitement du langage naturel (NLP) et l'intelligence artificielle pour offrir un support utilisateur automatisé, multilingue et contextuel.

Le chatbot est alimenté par **Groq LLM (Llama 3.8B)** intégré à **LlamaIndex**, permettant une compréhension profonde et des réponses précises adaptées à chaque utilisateur.

---

## ✨ Fonctionnalités Principales

### 🧠 Intelligence Artificielle & NLP
- **Intégration Groq LLM** : Utilise le modèle Llama 3.8B pour une compréhension contextuelle avancée
- **LlamaIndex Framework** : Architecture moderne pour la gestion de documents et requêtes complexes
- **Traitement Multilingue** : Répond en arabe, français, anglais, espagnol et autres langues
- **Détection Automatique de Langue** : Identifie la langue de l'utilisateur et répond dans la même langue
- **Recherche Sémantique** : Compréhension profonde du sens, pas seulement des mots-clés

### 📚 Système de FAQ Intelligent
- **Correspondance Approximative** : Utilise `difflib.get_close_matches()` pour trouver les réponses similaires
- **10+ Questions Fréquentes** : Base de connaissances pré-configurée sur AN-ETAT
- **Seuil de Confiance** : Cutoff de 0.7 pour garantir la pertinence des réponses
- **Réponses Contextualisées** : Informations précises sur les services, horaires et contacts

### 🔐 Sécurité & Architecture
- **API REST Sécurisée** : Endpoints POST avec validation CSRF
- **Gestion des Erreurs** : Gestion complète des exceptions JSON et API
- **Variables d'Environnement** : Gestion sécurisée des clés API via `.env` et `python-dotenv`
- **CORS Headers** : Authentification cross-origin pour intégration multidomaine
- **DRF Permissions** : Django REST Framework avec permissions AllowAny configurables

### 🎨 Interface Utilisateur
- **Frontend Interactif** : Interface HTML/CSS/JavaScript responsive
- **Design Moderne** : Styles CSS personnalisés (3083 bytes)
- **Chat en Temps Réel** : Communication asynchrone avec le serveur
- **UX Intuitive** : Interface conviviale et accessible

### 📖 Système de Prompt Avancé
- **Prompt Synthesis** : Prompt sophistiqué guidant l'IA pour des réponses professionnelles
- **Instructions Multilingues** : Guide l'IA à répondre dans la langue de l'utilisateur
- **Contexte AN-ETAT** : Intégration de l'information institutionnelle directement dans le prompt
- **Fallback Intelligent** : Introduction AN-ETAT comme réponse par défaut

### 📊 Gestion des Données
- **Base de Données SQLite** : Stockage léger et intégré
- **Django ORM** : Gestion de base de données flexible et sécurisée
- **Migrations Automatiques** : Schéma de base de données versionné

---

## 🛠️ Technologies Utilisées

| Technologie | Utilisation | Version |
|---|---|---|
| **Python** | Langage de programmation principal | 3.10+ |
| **Django** | Framework web backend | 5.1.3 |
| **Django REST Framework** | API REST avancée | 3.15.2 |
| **Groq LLM** | Modèle IA Llama 3.8B | Latest |
| **LlamaIndex** | Framework indexation & RAG | 0.12.19 |
| **OpenAI** | Support API alternative | 1.63.2 |
| **BeautifulSoup4** | Web scraping & parsing | 4.13.3 |
| **NLTK** | Traitement langage naturel | 3.9.1 |
| **Pandas** | Analyse de données | 2.2.3 |
| **Pillow** | Traitement d'images | 10.2.0 |
| **SQLAlchemy** | ORM avancé | 2.0.38 |
| **Pydantic** | Validation de données | 2.10.6 |
| **CORS Headers** | Gestion cross-origin | 4.7.0 |
| **python-dotenv** | Gestion variables environnement | 1.0.1 |
| **Transformers** | Modèles NLP pré-entraînés | 4.49.0 |

---

## 🏗️ Architecture du Projet

```
chatbot/
├── chatbot/                          # Application Django principale
│   ├── views.py                      # Logique API du chatbot (6374 bytes)
│   │   ├── chatbot_view()            # Endpoint POST pour réponses IA
│   │   ├── chatbot_test_view()       # Endpoint test interface
│   │   ├── FAQ dictionary            # 10+ questions préchargées
│   │   └── prompt_synthesis          # Prompt system avancé
│   ├── urls.py                       # Routing des endpoints
│   ├── admin.py                      # Admin Django
│   ├── apps.py                       # Configuration application
│   ├── models.py                     # Modèles de données
│   ├── tests.py                      # Tests unitaires
│   ├── migrations/                   # Migrations base de données
│   └── templates/
│       └── chatbot/
│           └── chatbot_test.html     # Interface frontend
│
├── chatbot_django/                   # Configuration Django
│   ├── settings.py                   # Configuration Django complète
│   ├── urls.py                       # Routage global
│   ├── asgi.py                       # Interface ASGI
│   └── wsgi.py                       # Interface WSGI
│
├── static/                           # Fichiers statiques
│   ├── styles.css                    # Styles interface (3083 bytes)
│   └── images/                       # Ressources images
│
├── manage.py                         # Script gestion Django
├── requirements.txt                  # Dépendances Python (102 packages)
├── .env                              # Variables environnement
├── .gitignore                        # Fichiers à ignorer
├── chatbot.gif                       # Démonstration GIF
└── db.sqlite3                        # Base de données
```

---

## 🚀 Installation & Configuration

### Prérequis
- **Python** 3.10 ou supérieur
- **pip** (gestionnaire de packages)
- **Groq API Key** (obtenir sur https://console.groq.com)
- **Git**

### Étapes d'Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/saleck24/chatbot.git
   cd chatbot
   ```

2. **Créez un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez les variables d'environnement :**
   - Créez ou modifiez le fichier `.env` :
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Appliquez les migrations :**
   ```bash
   python manage.py migrate
   ```

6. **Démarrez le serveur de développement :**
   ```bash
   python manage.py runserver
   ```

7. **Accédez à l'application :**
   - Interface test : `http://localhost:8000/chatbot-test/`
   - API endpoint : `http://localhost:8000/api/chatbot/`

---

## 📡 API REST

### Endpoint Principal

**POST** `/api/chatbot/`

#### Request
```json
{
  "question": "Quels sont les services de l'AN-ETAT ?"
}
```

#### Response (Succès)
```json
{
  "response": "L'AN-ETAT offre des services numériques comme l'e-administration, la cybersécurité et la gestion des infrastructures IT."
}
```

#### Response (Erreur)
```json
{
  "error": "Veuillez poser une question."
}
```

### Validations
- Méthode : `POST` uniquement
- Content-Type : `application/json`
- Permissions : `AllowAny` (configurable)
- Gestion CSRF : Activée par défaut

---

## 🧪 Exemple d'Utilisation

### Avec cURL
```bash
curl -X POST http://localhost:8000/api/chatbot/ \
  -H "Content-Type: application/json" \
  -d '{"question": "Parlez-moi de l'AN-ETAT"}'
```

### Avec Python
```python
import requests
import json

url = "http://localhost:8000/api/chatbot/"
data = {"question": "Quels sont les horaires d'ouverture ?"}

response = requests.post(url, json=data)
result = response.json()
print(result["response"])
```

### Avec JavaScript
```javascript
const question = "Comment contacter l'AN-ETAT ?";

fetch('/api/chatbot/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ question: question })
})
.then(response => response.json())
.then(data => console.log(data.response));
```

---

## 🎯 Cas d'Usage

✅ **Support Client Automatisé** : Répondre aux questions courantes 24/7  
✅ **Multilingue** : Support en arabe, français, anglais et espagnol  
✅ **FAQ Intelligent** : Correspondance approximative pour questions similaires  
✅ **IA Contextuelle** : Réponses adaptées au contexte institutionnel AN-ETAT  
✅ **Recherche Sémantique** : Compréhension du sens, pas seulement des mots-clés  
✅ **Intégration Web** : Déploiement facile sur n'importe quel site  

---

## 💡 Points Forts du Projet

✅ **IA de Pointe** : Utilisation du modèle Llama 3.8B via Groq  
✅ **Architecture Modulaire** : Séparation clean entre backend et frontend  
✅ **API RESTful** : Endpoint standard et bien documenté  
✅ **Multilingue** : Gestion native de plusieurs langues  
✅ **Sécurité** : Gestion d'environnement, validation CSRF, gestion d'erreurs  
✅ **Scalabilité** : Django permet facilement l'évolution du projet  
✅ **Documentation Complète** : Code commenté et README détaillé  
✅ **Interface Responsive** : Frontend moderne et accessible  
✅ **Prompt Engineering** : Système de prompt avancé pour réponses précises  
✅ **Gestion des Dépendances** : 102 packages optimisés et à jour  

---

## 🔧 Configuration Avancée

### Modifier le Modèle IA
```python
# Dans chatbot/views.py
llm = Groq(model="llama3-70b-8192", api_key=GROQ_API_KEY)  # Plus puissant mais plus lent
```

### Ajouter des Questions FAQ
```python
FAQ = {
    "Nouvelle Question ?": "Nouvelle réponse",
    # ... autres questions
}
```

### Déploiement Production
1. Mettez `DEBUG = False` dans `settings.py`
2. Configurez `ALLOWED_HOSTS`
3. Utilisez une base de données PostgreSQL
4. Configurez HTTPS et CORS correctement
5. Déployez avec Gunicorn + Nginx

---

## 📚 Apprentissages & Compétences Développées

- **IA & Machine Learning** : Intégration de modèles LLM dans applications web
- **NLP Avancé** : Traitement multilingue et détection de langue
- **Django & DRF** : Framework web complet et API REST professionnelle
- **Architecture API** : Design d'endpoints sécurisés et performants
- **Prompt Engineering** : Création de prompts sophistiqués pour contrôler l'IA
- **Frontend-Backend** : Intégration complète interface et serveur
- **Gestion d'Erreurs** : Handling d'exceptions et validations robustes
- **Déploiement Web** : Configuration WSGI, ASGI et serveurs web
- **Sécurité** : Protection CSRF, gestion des clés API, validation des entrées
- **DevOps** : Gestion d'environnement, dépendances, versioning

---

## 🎬 Démo

Une démonstration GIF du chatbot est disponible : `chatbot.gif`

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 🌐 Ressources & Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [LlamaIndex](https://docs.llamaindex.ai/)
- [Groq API](https://console.groq.com/docs)
- [NLTK](https://www.nltk.org/)

---
