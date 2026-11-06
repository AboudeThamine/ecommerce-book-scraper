# E-Commerce Book Catalog Web Scraper

A lightweight, automated Python scraper that navigates through multi-page e-commerce catalogs, parses item details using BeautifulSoup, and exports structured product data directly into a CSV spreadsheet.

## Features
- **Pagination Handling:** Iterates through multiple catalog pages automatically.
- **Data Sanitization:** Strips HTML whitespace, currency characters, and non-numeric artifacts.
- **CSV Pipeline:** Formats output into structured columns (`Title`, `Price (GBP)`, `Status`) ready for Excel or Google Sheets.

## Tech Stack
- **Python 3**
- **Requests** (HTTP page requests)
- **BeautifulSoup4** (DOM parsing)

## How to Run

1. **Activate your environment and install dependencies:**
   ```bash
   pip install -r requirements.txt