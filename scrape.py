import re
from bs4 import BeautifulSoup
import requests

def getItems(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    item_divs = soup.find_all("div", class_="item wow zoomIn")
    item_list = []
    for item_div in item_divs:
        content_div = item_div.find("div", class_="content")
        img_div = item_div.find("div", class_="img")
        price_text = content_div.span.get_text(strip=True)
        price = float(price_text[3:].replace(',', ''))
        img_div_style = re.findall('url\((.*?)\)', img_div['style'])[0]
        item_dict = {
            "name": content_div.h4.get_text(strip=True),
            "description": img_div.span.get_text(strip=True),
            "price": price,
            "image_url": img_div_style,
        }
        item_list.append(item_dict)
    return item_list

def getCategories(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    category_heading = soup.find('h2', class_='heading wow fadeInUp')
    return category_heading.string

getItems('https://kfc.ke/item?ItemSearch%5Bcategory%5D=hawugh3xujtc0407&ItemSearch%5Bday%5D=7')