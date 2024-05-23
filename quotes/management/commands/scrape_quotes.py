import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from quotes.models import Quote
import time

class Command(BaseCommand):
    help = 'Scrape quotes from Goodreads and save them to the database'

    def handle(self, *args, **kwargs):
        url = 'https://www.goodreads.com/quotes'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching the page: {e}'))
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quoteDetails')

        for quote in quotes:
            try:
                text = quote.find('div', class_='quoteText').get_text(strip=True).split('”')[0] + '”'
                author = quote.find('span', class_='authorOrTitle').get_text(strip=True)
                source = url

                # Print extracted data for debugging
                print(f'Text: {text}, Author: {author}')

                Quote.objects.create(text=text, author=author, source=source)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing quote: {e}'))

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved quotes'))
