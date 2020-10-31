""" Script that will import the data from the OpenFoodFacts API and feed the Database."""
import mysql.connector
import pprint
import requests
from param import parameters


def main():
    import json
    with open('./settings.json', 'r') as settings:
        data = json.load(settings)
    db = mysql.connector.connect(
        host=parameters["host"],
        user=parameters["user"],
        passwd=parameters["password"],
        database=parameters["database"])
    cursor = db.cursor()

    

    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()
    i = 1
    junction = []
    for category in categories:
        url = f'''https://world.openfoodfacts.org/cgi/search.pl?search_terms={category}&search_simple=1&action=process&json=1&page={data['page']}&page_size={data['page_size']}'''
        json = requests.get(url).json()
        raw_products = json['products']
        for raw_product in raw_products:
            cursor.execute("INSERT INTO Product (name_product, quantity, id_category,\
                nutri_score, ingredients, link_url, stores) VALUES(%s,%s,%s,%s,%s,%s,%s);",
                (raw_product['product_name'], raw_product['quantity'], category[0], raw_product['nutriscore_grade'],
                raw_product['ingredients_text_fr'], raw_product['url'], raw_product['stores']))
            if raw_product['stores_tags']:
                for store in raw_product['stores_tags']:
                    cursor.execute("INSERT INTO store (name) VALUES (%s);", (store,))
                    junction.append([i, raw_product['product_name'], store])
            i += 1
    db.commit()

    cursor.execute("DELETE store FROM store LEFT OUTER JOIN (SELECT MIN(id) as id, name FROM store GROUP BY name) AS table_1 ON store.id = table_1.id WHERE table_1.id IS NULL;")
    db.commit()

    for line in junction:
        cursor.execute("INSERT INTO junction_store_product (id_product, id_store) VALUES(%s,(SELECT id FROM Store WHERE Store.name = %s));", (line[0], line[2]))
    db.commit()
