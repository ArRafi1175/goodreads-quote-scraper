import requests
from bs4 import BeautifulSoup
import json
import time

# Author name and their Goodreads author ID
authors = {
    "Franz Kafka": "5223",
    "Fyodor Dostoevsky": "3137322",
    "Sylvia Plath": "4379",
    "Albert Camus": "957894",
    "Osamu Dazai": "113561",
    "Friedrich Nietzsche": "1938",
    "Aristotle": "2192",
    "Chekhov": "5031025",
    "Kierkegaard": "6172",
    "Marcus Aurelius": "17212",
    "Oscar Wilde": "3565",
    "Plato": "879",
    "Rumi": "875661",
    "Sartre": "1466",
    "Seneca": "4918776",
    "Simone de Beauvoir": "5548",
    "Thoreau": "10264",
    "Tolstoy": "128382",
    "Virginia Woolf": "6765",
}

# Tag to mood mapping
TAG_MOOD_MAP = {
    "love": "happy",
    "joy": "happy",
    "happiness": "happy",
    "books": "happy",
    "smile": "happy",
    "beauty": "inspirational",
    "hope": "inspirational",
    "soul": "inspirational",
    "strength": "inspirational",
    "courage": "inspirational",
    "philosophy": "inspirational",
    "wisdom": "inspirational",
    "life": "inspirational",
    "death": "tragic",
    "suicide": "tragic",
    "pain": "tragic",
    "suffering": "tragic",
    "despair": "tragic",
    "loneliness": "sad",
    "darkness": "sad",
    "sadness": "sad",
    "melancholy": "sad"
}

# Get mood from tags
def get_mood_from_tags(tags):
    for tag in tags:
        if tag in TAG_MOOD_MAP:
            return TAG_MOOD_MAP[tag]
    return "sad"  # default

# User agent to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_quotes = []

# Scrape each author's quote pages
for author, author_id in authors.items():
    print(f"Scraping quotes from {author}...")
    for page in range(1, 31):  # Change page count if needed
        url = f"https://www.goodreads.com/author/quotes/{author_id}?page={page}"
        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            print(f"Failed to load page {page} for {author}")
            continue

        soup = BeautifulSoup(res.text, 'html.parser')
        quote_blocks = soup.find_all("div", class_="quote")

        for quote in quote_blocks:
            # Extract quote text
            text_div = quote.find("div", class_="quoteText")
            if not text_div:
                continue

            text_raw = text_div.get_text(separator=" ").strip()
            quote_text = text_raw.split("―")[0].strip('“” ').strip()

            # Extract tags
            tags_div = quote.find("div", class_="greyText smallText left")
            tags = []
            if tags_div:
                tag_links = tags_div.find_all("a")
                tags = [a.get_text(strip=True).lower() for a in tag_links]

            mood = get_mood_from_tags(tags)

            all_quotes.append({
                "text": quote_text,
                "author": author,
                "mood": mood
            })

        time.sleep(2)  # Pause between pages

# Save to JSON
with open("goodreads_quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, ensure_ascii=False, indent=4)

print(f"Scraped {len(all_quotes)} quotes.")