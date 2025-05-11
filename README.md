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
