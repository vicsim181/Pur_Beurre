import mysql.connector
from param import parameters
import json

with open('./settings.json', 'r') as settings:
    data = json.load(settings)

db = mysql.connector.connect(
    host=parameters["host"],
    user=parameters["user"],
    passwd=parameters["password"],
    database=parameters["database"])

cursor = db.cursor()

for category in data['categories']:
    cursor.execute("INSERT INTO Category (category_name) VALUES (%s);", (category,))
    db.commit()