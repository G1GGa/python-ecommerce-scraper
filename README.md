# Python E-Commerce Web Scraper

A lightweight and robust web scraper built with Python, `requests`, and `BeautifulSoup` to extract product data (names and prices) from e-commerce test sites and export it into a structured CSV file.

## 🚀 Features
* Sends HTTP GET requests to target websites.
* Parses HTML content cleanly using `BeautifulSoup`.
* Cleans extracted text data using `.strip()` to remove unwanted whitespaces and formatting issues.
* Organizes scraped data into Python dictionaries and lists.
* Exports data cleanly into a **CSV file** using `csv.DictWriter` with UTF-8 encoding.

## 🛠️ Tech Stack
* **Python** (Core logic)
* **Requests** (HTTP client)
* **BeautifulSoup4** (HTML parsing)
* **CSV Module** (Data export)

## 📦 How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/python-ecommerce-scraper.git](https://github.com/YOUR-USERNAME/python-ecommerce-scraper.git)
