# Utiliser une image Python officielle
FROM python:3.11-slim

# Empêcher Python de générer des fichiers .pyc et activer le mode non-interactif
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn whitenoise

# Copier le reste du projet
COPY . .

# Rassembler les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port de Django
EXPOSE 8000

# Commande pour lancer les migrations et démarrer le serveur
CMD python manage.py migrate && gunicorn chatbot_django.wsgi:application --bind 0.0.0.0:8000
