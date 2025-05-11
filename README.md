# Goodreads Quote Scraper

This Python script scrapes quotes from a curated list of philosophers and literary authors on [Goodreads](https://www.goodreads.com), categorizes them by mood using tags, and saves the output as a JSON file.

## 📌 Features

- Scrapes quotes from authors like Kafka, Dostoevsky, Sylvia Plath, and others
- Extracts tags and maps them to moods (e.g., sad, happy, inspirational)
- Outputs data to `goodreads_quotes.json`
- Designed to be simple and extensible

## 📂 Output Format

The generated `goodreads_quotes.json` file will contain entries like:

```json
{
    "text": "Man is what he wills himself to be.",
    "author": "Sartre",
    "mood": "inspirational"
}
```
🛠️ Requirements
• Python 3.x
• requests
• beautifulsoup4

Install the dependencies using:
```bash
pip install -r requirements.txt
```
🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/goodreads-quote-scraper.git
cd goodreads-quote-scraper
```
2. Run the script:
```bash
python goodreads_scraper.py
```
Quotes will be saved in goodreads_quotes.json.

⚠️ Notes
• This script relies on Goodreads' public web pages and may break if the site structure changes.
• Be mindful of their terms of service when scraping content.
• Pages are scraped with a 2-second delay between each to reduce server load.

MADE BY RAIKI
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this code with proper attribution.
