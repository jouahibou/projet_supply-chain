from elasticsearch import Elasticsearch
import pandas as pd
import warnings

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline
import joblib

warnings.filterwarnings('ignore')


es = Elasticsearch(hosts = ["http://79.125.3.215:9200"])

query = {
    "query": {
        "match_all": {}
    },
    "size": 1000  # Adjust batch size as per your requirements
}

scroll = es.search(index="asurion", body=query, scroll="5m")
scroll_id = scroll["_scroll_id"]

hits = scroll["hits"]["hits"]
data = [hit["_source"] for hit in hits]

while len(hits) > 0:
    scroll = es.scroll(scroll_id=scroll_id, scroll="5m")
    hits = scroll["hits"]["hits"]
    data.extend([hit["_source"] for hit in hits])

df = pd.DataFrame(data)


df["text"] = df["titre"] + " " + df["comment"]
df["target"] = df["stars"].str[6]
df = df[["text", "target"]].copy()
df = df.dropna()
df["target"] = df["target"].astype(int)


def delete_punctiation(df, comment_col):
    """
    Removes punctuation from the specified column of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the text column.
        comment_col (str): The name of the column to remove punctuation from.

    Returns:
        None. The DataFrame is modified in-place.

    """
    pattern = r'[^a-zA-Z0-9\s]'
    df[comment_col] = df[comment_col].replace(pattern, ' ', regex=True)
    df[comment_col] = df[comment_col].str.replace('  ', ' ')


def truncate_text_column(df, column):
    df[column] = df[column].apply(lambda x: ' '.join(x.split()[:499]))
    return df


def text_cleaner(column):
    df[column] = df[column].str.lower() \
                            .str.strip() \
                            .str.replace(r'\s+', ' ')


text_cleaner("text")
delete_punctiation(df, "text")
truncate_text_column(df, 'text')

X = df["text"]
y = df["target"]

# Train the classifier
clf_final = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to numerical features using a Bag-of-Words approach
    ('classifier', MultinomialNB())  # Train a Multinomial Naive Bayes classifier
])

clf_final.fit(X, y)
joblib.dump(clf_final, 'mnb_final_model.joblib')