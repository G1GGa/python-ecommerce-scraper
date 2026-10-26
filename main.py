import csv
import requests
from bs4 import BeautifulSoup

get_request = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
bs = BeautifulSoup(get_request.text, "html.parser")
find_all_element = bs.find_all('div', class_='thumbnail')
box = []

for element in find_all_element:
    dictionary = {
        "names": element.find(class_ = "title").text.strip(),
        "prices": element.find("h4", class_ = "price").text.strip()
    }
    box.append(dictionary)

with open("products.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["names", "prices"])
    writer.writeheader()  
    writer.writerows(box)

