# Utiliser une image Python officielle basée sur Alpine
FROM python:3.13-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances (avec quelques packages nécessaires pour Alpine)
RUN apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port utilisé par Gradio (par défaut 7860)
EXPOSE 7860

# Commande pour lancer l'application Gradio
CMD ["python", "frontend/app_interface.py"]