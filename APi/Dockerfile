# Utilisez l'image Python 3.9 comme image de base
FROM python:3.9-slim-buster

# Copiez le code FastAPI dans le conteneur
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Installez les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port 8000 pour l'API FastAPI
EXPOSE 8000

# Démarrez l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]