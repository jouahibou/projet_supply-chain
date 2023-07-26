FROM python:3.9

# Définissez le répertoire de travail
WORKDIR /app/APi

# Copiez les fichiers de votre projet dans le conteneur
COPY . .

RUN echo "DefaultLimitNPROC=2048" >> /etc/systemd/system.conf

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port 80 pour FastAPI et le port 8501 pour Streamlit
EXPOSE 8080
EXPOSE 8501

# Démarrez l'application FastAPI avec uvicorn et Streamlit avec streamlit
CMD ["sh", "-c", "uvicorn APi.main:app --host 0.0.0.0 --port 8080 --workers 1 & streamlit run APi/stremlit.py --server.port 8501"]