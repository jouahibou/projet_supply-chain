FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./APi/main.py /app/main.py
COPY ./Scripts /app/Scripts
COPY ./requirements.txt /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# Ajouter cette ligne pour exécuter le script Python
RUN python /app/Scripts/upload_asurion_data_elasticsearch.py

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]