FROM python:3.9

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de votre projet dans le conteneur
COPY . .

RUN echo "DefaultLimitNPROC=2048" >> /etc/systemd/system.conf

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port 80 pour FastAPI et le port 8501 pour Streamlit
EXPOSE 80
EXPOSE 8501

# Lancez les commandes pour démarrer l'application
RUN python Scripts/upload_asurion_data_elasticsearch.py &
RUN uvicorn APi.main:app --port=80 &
RUN streamlit run APi/stremlit.py --server.port 8501