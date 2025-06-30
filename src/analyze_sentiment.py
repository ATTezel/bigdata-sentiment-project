import json
import pandas as pd
from textblob import TextBlob
import os

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return pd.Series([sentiment, polarity, subjectivity])

def main():
    with open("data/reddit_raw.json", "r") as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    df['text'] = df['title'] + " " + df['selftext']
    df[['sentiment', 'polarity', 'subjectivity']] = df['text'].apply(analyze_sentiment)

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/sentiment_results.csv", index=False)

    summary = {
        "positive": int((df['sentiment'] == "positive").sum()),
        "negative": int((df['sentiment'] == "negative").sum()),
        "neutral": int((df['sentiment'] == "neutral").sum())
    }

    with open("outputs/summary.json", "w") as f:
        json.dump(summary, f, indent=4)

if __name__ == "__main__":
    main()
