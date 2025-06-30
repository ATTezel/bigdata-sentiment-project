import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    df = pd.read_csv("outputs/sentiment_results.csv")
    sentiment_counts = df['sentiment'].value_counts()

    os.makedirs("report", exist_ok=True)
    plt.figure(figsize=(6, 4))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title("Sentiment Distribution of Reddit Posts")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("report/sentiment_plot.png")
    print("[+] Sentiment plot saved to 'report/sentiment_plot.png'")

if __name__ == "__main__":
    main()
