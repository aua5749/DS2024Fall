import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
DEFAULT_SLEEP = 3.0
SIGMA = 1.0
DOMAIN = 'http://books.toscrape.com'
STATE_FILENAME = 'state.json'
OUTPUT_FILENAME = 'books.csv'


def get(url: str) -> requests.Response:
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    print(f"Fetching URL: {url}")
    return requests.get(url, headers=HEADERS)


def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    with open(filename, 'w') as f:
        json.dump({'links': links, 'data': data}, f)
    print(f"State saved: {len(links)} links and {len(data)} books.")


def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
            links = state['links']
            data = state['data']
            if not links:
                links = ['/catalogue/category/books_1/index.html']
            print(f"Loaded state from {filename}: {len(links)} links and {len(data)} books.")
            return links, data
    except FileNotFoundError:
        print(f"No previous state found. Starting fresh.")
        return ['/catalogue/category/books_1/index.html'], {}


def write_spreadsheet(filename: str, data: dict[str, dict]) -> None:
    fieldnames = ['title', 'category', 'UPC', 'price', 'tax', 'availability', 'number of reviews']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in data.values():
            writer.writerow(book)
    print(f"Data written to {filename}: {len(data)} books.")

#to see what kind of pages
def is_book_page(url: str) -> bool:
    return '/catalogue/' in url and '/category/' not in url and 'index.html' not in url


def is_category_page(url: str) -> bool:
    return '/catalogue/category/' in url


if __name__ == '__main__':
    to_visit, data = load_state(STATE_FILENAME)

    print(f"Starting scraping with {len(to_visit)} links to visit and {len(data)} books already scraped.")

    # Added so there is always a starting point
    if not to_visit:
        to_visit.append('/catalogue/category/books_1/index.html')
        print("Added starting URL to empty to_visit list.")

    while to_visit:
        try:
            current_url = to_visit.pop(0)
            url = urljoin(DOMAIN, current_url)

            response = get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            if is_category_page(url):
                # This is category page, extract book links
                book_links = soup.select('h3 > a')
                for link in book_links:
                    book_url = urljoin(url, link['href'])
                    if book_url not in data and book_url not in to_visit:
                        to_visit.append(book_url)
                print(f"Found {len(book_links)} book links on category page: {url}")

                # Check for next page in category
                next_page = soup.select_one('li.next > a')
                if next_page:
                    next_url = urljoin(url, next_page['href'])
                    if next_url not in to_visit:
                        to_visit.append(next_url)
                        print(f"Added next category page: {next_url}")

            elif is_book_page(url):
                # This is a book page, extract book data
                if url in data:
                    print(f"Skipping already scraped book: {url}")
                    continue

                title = soup.find('h1').text.strip()
                category = soup.select('ul.breadcrumb li')[2].text.strip()
                upc = soup.select_one('th:contains("UPC") + td').text.strip()
                price = soup.select_one('th:contains("Price (incl. tax)") + td').text.strip()
                tax = soup.select_one('th:contains("Tax") + td').text.strip()
                availability = soup.select_one('th:contains("Availability") + td').text.strip()
                num_reviews = soup.select_one('th:contains("Number of reviews") + td').text.strip()

                data[url] = {
                    'title': title,
                    'category': category,
                    'UPC': upc,
                    'price': price,
                    'tax': tax,
                    'availability': availability,
                    'number of reviews': num_reviews
                }
                print(f"Scraped book data for: {title}")

            if len(data) % 10 == 0:  # Save state every 10 books
                save_state(STATE_FILENAME, to_visit, data)

        except KeyboardInterrupt:
            print("Process interrupted by user.")
            break
        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue

    save_state(STATE_FILENAME, to_visit, data)
    print(f"Scraping completed. Total books scraped: {len(data)}")
    write_spreadsheet(OUTPUT_FILENAME, data)
