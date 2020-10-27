""" Script that will import the data from the OpenFoodFacts API and feed the Database."""
import pprint
import requests
import mysql.connector
import json
from param import parameters

PAGE = 1
PAGE_SIZE = 85

with open('./settings.json', 'r') as settings:
    data = json.load(settings)

for category in data['categories']:    
    print(category)
    url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={category}&search_simple=1&action=process&json=1&page={PAGE}&page_size={PAGE_SIZE}'
    json = requests.get(url).json()
    raw_products = json['products']
    products = []
    i = 1
    for raw_product in raw_products:
        product = {'number' : i, 'nutriscore1' : raw_product["nutriscore_grade"],
        'nutriscore2' : raw_product["nutrition_grades"], 'name' : raw_product["product_name"],
        'url' : raw_product["url"],
        'ingredients' : raw_product["ingredients_text_fr"], 'quantity' : raw_product["quantity"]}
        products.append(product)
        i = i + 1

    conn = mysql.connector.connect(
        host=parameters["host"],
        user=parameters["user"],
        passwd=parameters["password"],
        database=parameters["database"]
    )
    mycursor = conn.cursor()
    mycursor.execute(
        "INSERT INTO Product("
    )