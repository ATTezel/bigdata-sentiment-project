# 📊 Social Media Sentiment Analysis of Strava via Reddit

This project performs a sentiment analysis of Reddit posts related to **Strava**, a leading fitness tracking platform. Using natural language processing (NLP) and Python-based tools, the analysis classifies public opinions into positive, negative, and neutral categories. The findings offer valuable insights into customer perception, trends, and potential areas of improvement.

---

## 🎯 Objective

- Collect Reddit posts about Strava using the Reddit API (via `praw`).
- Preprocess raw JSON data and perform sentiment classification using `TextBlob`.
- Visualize the results using `matplotlib` and `seaborn`.
- Derive actionable insights based on post polarity and subjectivity.

---

## 📁 Project Structure

```bash
bigdata_sentiment_project/
│
├── data/
│   └── reddit_raw.json                 # Raw Reddit data
│
├── outputs/
│   ├── sentiment_results.csv          # Sentiment results with metadata
│   ├── summary.json                   # Total counts per sentiment
│
├── report/
│   └── sentiment_plot.png             # Sentiment distribution chart
│
├── src/
│   ├── fetch_reddit.py                # Reddit API script
│   ├── analyze_sentiment.py          # Sentiment analysis logic
│   └── visualize_results.py          # Charting and visualization
│
├── requirements.txt
└── README.md
```

  🧪 Tools & Technologies
Category	Libraries / Tools
Data Collection	praw, json, requests
NLP / Analysis	TextBlob, NLTK, pandas
Visualization	matplotlib, seaborn
Environment	Python 3.9+ (venv), VS Code

  🚀 How to Run
Clone the repository

```bash
git clone https://github.com/ATTezel/bigdata-sentiment-project.git
cd bigdata-sentiment-project
Create virtual environment (optional)
```

```bash

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
Install required packages
```

```bash
pip install -r requirements.txt
Run the full pipeline
```

```bash
python src/fetch_reddit.py
python src/analyze_sentiment.py
python src/visuali  ze_results.py
```

📊 Sample Output
Sentiment Summary
```bash
{
  "positive": 19,
  "negative": 6,
  "neutral": 25
}
```
##Visualization

#📈 Data Example (CSV output)
title	text	sentiment	polarity	subjectivity
Introducing: Strava + Runna Subscription	Hey r/Strava! We’ve got...	positive	0.17	0.54
Feature Idea: Backwards Segments	When creating a segment...	neutral	0.0	0.0

#💡 Key Findings
Neutral sentiment dominates Reddit discussions about Strava (25/50 posts).

Positive sentiment (19/50) indicates general user satisfaction.

Negative sentiment (6/50) often relates to app limitations and subscription pricing.

The most mentioned themes include: subscriptions, segment features, and app updates.

#🧠 What I Learned
How to collect social media data using official APIs (Reddit with praw)

Basics of text-based sentiment classification using TextBlob

How to clean, analyze, and visualize unstructured data

Project documentation and structuring best practices for GitHub

👤 Author
Arda Tezel
Software Engineering Student – Big Data & Security Enthusiast
