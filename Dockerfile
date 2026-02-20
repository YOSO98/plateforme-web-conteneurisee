# Image Python officielle légère
FROM python:3.13-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l’application
COPY app/ .

# Variable d’environnement
ENV ENV=container

# Port exposé
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
