""" Script that will import the data from the OpenFoodFacts API and feed the Database."""
import pprint
import requests
import mysql.connector
import json
from param import parameters

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
# j = 1
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
                cursor.execute("INSERT INTO transfert (id_product, name_store) VALUES(%s,%s);", (i, store))
                # j += 1
                # junction.append([i, store])
        i += 1
db.commit()

cursor.execute("DELETE store FROM store LEFT OUTER JOIN (SELECT MIN(id) as id, name FROM store GROUP BY name) AS table_1 ON store.id = table_1.id WHERE table_1.id IS NULL;")
cursor.execute("DELETE store FROM store WHERE id IN (283, 62, 57, 432, 371, 389, 152);") #DELETE des id à modifier ou supprimer selon les données rentrées dans la table
db.commit()

cursor.execute("ALTER TABLE transfert (id_store) VALUES(store.id) WHERE (SELECT store.id FROM store INNER JOIN transfert ON transfert.name_store = store.name);")
db.commit()
cursor.execute("SELECT * FROM transfert;")
trans = cursor.fetchall()
for piece in trans:
    print(piece)

# cursor.execute("INSERT INTO junction_product_store (id_product, id_store) VALUES(SELECT product.id, store.id FROM );")

# id_store = cursor.execute("SELECT store.id FROM store WHERE store.name = (%s);", (element[1],))
# cursor.execute("INSERT INTO Junction_store_product (id_product, id_store) VALUES(%s,%s);", (element[0], element[1])

# cursor.execute("CREATE TRIGGER ")

# cursor.execute("DELETE store FROM store LEFT OUTER JOIN (\
#     SELECT MIN(id) as id, name FROM store GROUP BY name) AS table_1\
#     ON store.id = table_1.id WHERE table_1.id IS NULL;")
# cursor.execute("DELETE store FROM store WHERE id IN (\
#     283, 62, 57, 432, 371, 389, 152);") #DELETE des id à modifier ou supprimer selon les données rentrées dans la table
# db.commit()
