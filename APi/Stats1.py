import streamlit as st
from elasticsearch import Elasticsearch
import pandas as pd
import altair as alt
import numpy as np


def pages1():
    # Connexion à Elasticsearch
    es = Elasticsearch(hosts=["http://79.125.3.215:9200"])
    # Requête Elasticsearch pour récupérer les données
    res = es.search(index="asurion", body={"query": {"match_all": {}}})
    # Extraire les données des résultats de la requête
    hits = res['hits']['hits']
    data = [{"localisation": hit['_source']['localisation'], "stars": hit['_source']['stars']} for hit in hits]
    # Créer un DataFrame pandas à partir des données
    df = pd.DataFrame(data)
    # Calculer le pourcentage de commentaires pour chaque localisation
    percentage = df["localisation"].value_counts(normalize=True).reset_index()
    percentage.columns = ["localisation", "percentage"]
    # Créer un graphique à barres pour le pourcentage de commentaires par localisation
    bar_chart = alt.Chart(percentage).mark_bar().encode(
        x=alt.X('localisation:N', title='Localisation'),
        y=alt.Y('percentage:Q', title='Pourcentage de commentaires'),
        tooltip=['localisation', 'percentage']
    ).properties(
        width=600,
        height=400,
        title='Pourcentage de commentaires par localisation'
    )

    # Afficher le graphique à barres
    st.altair_chart(bar_chart)

    # Calculer le pourcentage de clients satisfaits et insatisfaits
    total_customers = len(df)
    satisfied = round((df["stars"].str.extract('(\d+(?:\.\d+)?)').astype(float) >= 4).sum() / total_customers * 100, 2)
    unsatisfied = round((df["stars"].str.extract('(\d+(?:\.\d+)?)').astype(float) < 4).sum() / total_customers * 100, 2)
    labels = ['Satisfaits', 'Insatisfaits']
    # Aplatir la liste sizes
    sizes = np.ravel([satisfied, unsatisfied])
    # Créer un graphique en camembert pour le nombre de clients satisfaits
    pie_chart = alt.Chart(pd.DataFrame({'labels': labels, 'sizes': sizes})).mark_arc().encode(
        theta='sizes:Q',
        color='labels:N',
        tooltip=['labels', 'sizes']
    ).properties(
        width=400,
        height=400,
        title='Proportion de clients satisfaits'
    )

    # Afficher le graphique en camembert
    st.altair_chart(pie_chart)