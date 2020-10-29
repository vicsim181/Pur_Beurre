""" Script holding the class that will import the data from the OpenFoodFacts API and feed the Database."""
import pprint
import requests
import mysql.connector
import json
from param import parameters

PAGE = 1
PAGE_SIZE = 80

class Extract_Feed_Db():
    """Class extracting the data from the OFF API."""
    def __init__(self):
        with open('./settings.json', 'r') as settings:
            self.data = json.load(settings)
        self.db = mysql.connector.connect(
            host=parameters["host"],
            user=parameters["user"],
            passwd=parameters["password"],
            database=parameters["database"])
        self.cursor = self.db.cursor()

    def extract_and_feed(self):
        """Function extracting the data from the API."""
        """Feeding the tables of the database."""
        i = 1
        for category in self.data['categories']:
            print(category)
            self.cursor.execute("INSERT INTO Category (category_name) VALUES (%s);", (category,))
            url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={category}&search_simple=1&action=process&json=1&page={PAGE}&page_size={PAGE_SIZE}'
            json = requests.get(url).json()
            raw_products = json['products']
            for index, raw_product in enumerate(raw_products):
                self.cursor.execute("INSERT INTO Product (name_product, quantity, id_category,\
                    nutri_score, ingredients, link_url) VALUES(%s,%s,%s,%s,%s,%s);",
                    (raw_product['product_name'], raw_product['quantity'], i, raw_product['nutriscore_grade'],
                    raw_product['ingredients_text_fr'], raw_product['url']))
                if raw_product['stores_tags']:
                    for store in raw_product['stores_tags']:
                        self.cursor.execute("INSERT INTO Store (name) VALUES (%s);", (store,))
            i += 1    
        self.db.commit()

    def sort_stores(self):
        """Function eliminating the doubles in the stores table"""
        self.cursor.execute("DELETE store FROM store LEFT OUTER JOIN (\
            SELECT MIN(id) as id, name FROM store GROUP BY name) AS table_1\
            ON store.id = table_1.id WHERE table_1.id IS NULL;")
        self.cursor.execute("DELETE store FROM store WHERE id IN (\
            283, 62, 57, 432, 371, 389, 152);") #DELETE des id à modifier ou supprimer selon les données rentrées dans la table
        self.db.commit()

dbextraction = Extract_Feed_Db()
dbextraction.extract_and_feed()
dbextraction.sort_stores()