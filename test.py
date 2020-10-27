import pprint
import mysql.connector
from param import parameters
import json
import requests

PAGE = 1
PAGE_SIZE = 80
category = '''apéritif'''
print(category)
url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={category}&search_simple=1&action=process&json=1&page={PAGE}&page_size={PAGE_SIZE}'
json = requests.get(url).json()
raw_products = json['products']
products = []
i = 1
for raw_product in raw_products:
    product = {'number' : i, 'nutriscore1' : raw_product["nutriscore_grade"],
    'nutriscore2' : raw_product["nutrition_grades"], 'name' : raw_product["product_name"],
    'url' : raw_product["url"], 'stores' : raw_product["stores_tags"],
    'ingredients' : raw_product["ingredients_text_fr"], 'quantity' : raw_product["quantity"]}
    products.append(product)
    i = i + 1
pprint.pprint(products)
