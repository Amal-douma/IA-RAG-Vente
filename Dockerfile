# ✅ Utilise une image Python légère basée sur Alpine Linux
FROM python:3.13-alpine

# ✅ Définit le répertoire de travail dans le conteneur
WORKDIR /app

# ✅ Copie le fichier de dépendances dans le conteneur
COPY requirements.txt .

# ✅ Installe les dépendances système nécessaires pour compiler certaines libs Python
# Ensuite installe les dépendances Python
RUN apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt

# ✅ Copie tous les fichiers du projet dans le conteneur
COPY . .

# ✅ Expose le port utilisé par Gradio
EXPOSE 7860

# ✅ Définit la commande par défaut pour lancer l’application
CMD ["python", "frontend/app_interface.py"]


# FROM python:3.11-alpine

# WORKDIR /app

# COPY requirements.txt .

# RUN apk add --no-cache gcc musl-dev freetype-dev libjpeg-turbo-dev zlib-dev && \
#     pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 7860

# CMD ["python", "Frontend/app_interface.py"]

