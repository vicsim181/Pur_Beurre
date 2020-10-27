""" Script that will import the data from the OpenFoodFacts API and feed the Database."""
import pprint
import requests
import mysql.connector

PAGE = 1
PAGE_SIZE = 100
PRODUCT = '''jus d'orange'''
url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={PRODUCT}&search_simple=1&action=process&json=1&page={PAGE}&page_size={PAGE_SIZE}'
json = requests.get(url).json()
raw_products = json['products']
products = []
for raw_product in raw_products:
    product = {'nutriscore' : raw_product["nutriscore_grade"], 'name' : raw_product["product_name"]}
    products.append(product)

pprint.pprint(products)
