import mysql.connector
from param import parameters

db = mysql.connector.connect(
    host=parameters["host"],
    user=parameters["user"],
    passwd=parameters["password"],
    database=parameters["database"])
cursor = db.cursor()

cursor.execute("DROP TABLE product, category, store, favorite, junction_store_product")