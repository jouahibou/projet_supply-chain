import pandas as pd
import warnings
import joblib

warnings.filterwarnings('ignore')

clf_final = joblib.load('mnb_final_model.joblib')

data = {'text': ["excellent service with any insurance claim you obviously have to explain the damage and click through the fraud acknowledgements, etc. that was not difficult at all.after that, the process was slick slick slick. the claim was filed late on a thursday afternoon and the replacement arrived on the friday morning.clear instructions the whole way and a very simple process",
                 "i never received the phone. you sent me a note last thursday that it was on its way. today is late tuesday night. still no phone. really frustrating.",
                 "absolutely disgusted with asurion - not trustworthy, no integrity i am completely disgusted with your company. a cell phone is an essential part of communication, and it is unacceptable for a simple glass replacement to take more than two weeks. from the first scheduled meeting to have the tech come to my home to repair (note that i had to reschedule appointments to be home), they canceled an hour after the scheduled arrival time. service truck was in the shop, multiple reschedule attempts - all failed to have the tech come to my home to fix the issue. five times after they were supposed to arrive, they cancelled! unacceptable. adam with ubreakifix. i finally caved and called at&t for assistance. they helped me get an appointment scheduled by contacting your company on my behalf... this time, there was no rescheduling; they simply did not show up, no call, no text.when i called, the asurion tech shipped the phone, promising that i would receive it the next day via fedex - lie, it arrived two days later. this has been the worst experience - your company's customer service is worse than comcast/xfinity's. satan trained ineffective employees. you're the worst!"]}
df = pd.DataFrame(data, columns=['text'])

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

print(clf_final.predict(df["text"]))