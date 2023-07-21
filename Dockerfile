# Utilisez l'image Python 3.9 comme image de base
FROM python:3.9

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de votre projet dans le conteneur
COPY . .

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port 80 pour FastAPI et le port 8501 pour Streamlit
EXPOSE 80
EXPOSE 8501

# Commande pour lancer le script upload_asurion_data_elasticsearch.py et démarrer l'application
CMD ["bash", "-c", "python Scripts/upload_asurion_data_elasticsearch.py & uvicorn APi.main:app  --port=80 & streamlit run APi/stremlit.py --server.port 8501"]