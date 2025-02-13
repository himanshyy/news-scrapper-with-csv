import requests
import csv
from bs4 import BeautifulSoup


# Function to scrape headlines and links
def scrape_news(url):
    """Scrapes headlines and links from a user-provided news website."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error fetching {url}: Status Code {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    
    # Extract headlines and links from <a> tags
    articles = soup.find_all("a")  # Finding all anchor tags (generic approach)
    for article in articles[:10]:  # Limiting to top 10 headlines
        headline = article.get_text(strip=True)
        link = article["href"] if article.has_attr("href") else ""
        if headline and link:
            headlines.append((headline, link))
    
    return headlines if headlines else "No headlines found. Try another URL."

# Ask user for a news website URL
user_url = input("Enter a news website URL: ")

# Scrape news from user-provided URL
news = scrape_news(user_url)

# Save results to CSV
csv_filename = "news_headlines3.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Headline", "Link"])
    
    if isinstance(news, list):
        csv_writer.writerows(news)
    else:
        csv_writer.writerow([news, ""])

print("\nTop News Headlines:")


print(f"\nNews headlines with links have been saved to {csv_filename}")
#bbc=https://www.bbc.com/news
#CNN=https://edition.cnn.com/world
#NDTV=https://www.ndtv.com/world-news"