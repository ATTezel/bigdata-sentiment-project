import praw
import json
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")


def fetch_reddit_data(subreddit='strava', limit=100):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "selftext": post.selftext,
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "url": post.url
        })
    return posts

def save_json(posts, filepath="data/reddit_raw.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)
    print(f"[+] {len(posts)} posts saved to {filepath}")

if __name__ == "__main__":
    posts = fetch_reddit_data(limit=50)
    save_json(posts)
