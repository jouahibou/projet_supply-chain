import plotly.express as px
import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
#from import_es_data import import_data_from_es

def filter_by_rating(df):
    df = df.dropna(subset=['stars'])
    # Convert 'stars' column to strings to avoid type errors
    df['stars'] = df['stars'].astype(str)
    # Sidebar for filtering by rating
    st.sidebar.title("Filter by Rating")
    rating_filter = st.sidebar.multiselect("Select rating(s)", sorted(df['stars'].unique()))
    # Filter the data based on the selected rating(s)
    if rating_filter:
        filtered_df = df[df['stars'].isin(rating_filter)]
    else:
        filtered_df = df

    # Display the filtered data
    st.subheader("Filtered Data")
    st.write(filtered_df)

    # Plot the distribution of ratings
    st.subheader("Distribution of Ratings")
    rating_counts = filtered_df['stars'].value_counts().reset_index()
    rating_counts.columns = ['stars', 'count']
    chart = alt.Chart(rating_counts).mark_bar().encode(
        x=alt.X('stars', axis=alt.Axis(labelAngle=-45)),
        y='count'
    ).properties(
        width=alt.Step(40)
    )
    st.altair_chart(chart, use_container_width=True)

def show_comment_distri_by_stars(df):
    df = df.dropna()
    df = df[df['stars'] != '']
    df["stars"] = df["stars"].str[6].astype(int)

    df_rating_distr = df.groupby('stars').size().reset_index(name='nb_comments')

    fig = px.bar(df_rating_distr, x='stars', y='nb_comments', text='nb_comments',
             title='Distribution of comments by ratings',
             labels={'stars': 'Rating', 'nb_comments': 'Number of comments'})
    
    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig, use_container_width=True)

def show_comment_distri_by_loc(df):
    df = df.dropna()
    df = df[df['localisation'] != '']
    df_loc_distr= df.groupby('localisation').size().reset_index(name='nb_comments')
    df_loc_distr = df_loc_distr.nlargest(5, 'nb_comments')
    fig = px.bar(df_loc_distr, x='localisation', y='nb_comments', text='nb_comments',
             title='Distribution of comments by localisation (on a LOG scale)',
             labels={'localisation': 'Country', 'nb_comments': 'Number of comments'})
    st.plotly_chart(fig, use_container_width=True)

def plot_review_timeline(df, rating_filter=None):
    # Filtrer les données en fonction de la note sélectionnée (si applicable)
    if rating_filter is not None:
        df = df[df['stars'] == rating_filter]

    # Convertir la colonne date_review en datetime
    df['date_review'] = pd.to_datetime(df['date_review'])

    # Extraire les années à partir de la colonne date_review
    df['year'] = df['date_review'].dt.year

    # Créer un graphique en barres avec l'année en tant qu'axe X et le nombre de commentaires pour chaque année en tant qu'axe Y
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('year:O',axis=alt.Axis(labelAngle=-45),title='Année'),
        y=alt.Y('count()', title='Number of comments'),
        tooltip=[alt.Tooltip('year:O', title='Année'), alt.Tooltip('count()', title='Nombre de commentaires')]
    ).properties(
        title={
            'text': 'timeline of comments',
            'subtitle': f"Total number of comments: {df.shape[0]}"
        }
    )
    # Afficher le graphique
    altair_plot = st.altair_chart(chart, use_container_width=True)
    return altair_plot

