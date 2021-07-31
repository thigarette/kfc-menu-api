from bs4 import BeautifulSoup
import requests
streetwise_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=hawugh3xujtc0407&ItemSearch%5Bday%5D=7'
snacks_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=0anomwm9jcnozryg&ItemSearch%5Bday%5D=7'
sharing_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=njl5ulycgg8ft5rv&ItemSearch%5Bday%5D=7'
chicken_deals_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=c5x4llcdlwtk0nok&ItemSearch%5Bday%5D=7'
side_items_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=hrg3adkvuhe68spw&ItemSearch%5Bday%5D=7'
drinks_url = 'https://kfc.ke/item?ItemSearch%5Bcategory%5D=0ffdg0xcq9ebcicn&ItemSearch%5Bday%5D=7'

def getItems(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    item_divs = soup.find_all("div", class_="item wow zoomIn")
    for item_div in item_divs:
        print(item_div.div.span.string)

getItems(drinks_url)