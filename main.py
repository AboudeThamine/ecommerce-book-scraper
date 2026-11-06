import csv
import time
import requests
from bs4 import BeautifulSoup

def scrape_books(max_pages=3):
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    all_books = []

    print(f"Starting scrape for the first {max_pages} pages...\n")

    for page_num in range(1, max_pages + 1):
        target_url = base_url.format(page_num)
        print(f"Fetching: {target_url}")

        response = requests.get(target_url, headers=headers)

        if response.status_code != 200:
            print(f"Warning: Could not fetch page {page_num} (Status: {response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        book_cards = soup.find_all("article", class_="product_pod")

        for card in book_cards:
            title_tag = card.find("h3").find("a")
            title = title_tag["title"] if title_tag else "N/A"

            raw_price = card.find("p", class_="price_color").text.strip()
            clean_price = raw_price.replace("£", "").replace("Â", "")

            availability_tag = card.find("p", class_="instock availability")
            availability = availability_tag.text.strip() if availability_tag else "Unknown"

            all_books.append({
                "Title": title,
                "Price (GBP)": clean_price,
                "Status": availability
            })

        time.sleep(1)

    output_filename = "books_catalog.csv"
    with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price (GBP)", "Status"])
        writer.writeheader()
        writer.writerows(all_books)

    print(f"\nCompleted! Scraped {len(all_books)} books and saved to '{output_filename}'.")

if __name__ == "__main__":
    scrape_books(max_pages=3)