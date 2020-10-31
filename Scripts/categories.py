import mysql.connector
from param import parameters
import json

db = mysql.connector.connect(
        host=parameters["host"],
        user=parameters["user"],
        passwd=parameters["password"],
        database=parameters["database"])
cursor = db.cursor()

with open('./settings.json', 'r') as settings:
    data = json.load(settings)

for category in data['categories']:
    cursor.execute("INSERT INTO Category (category_name) VALUES (%s);", (category,))
db.commit()
