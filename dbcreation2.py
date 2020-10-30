"""Script hosting the class allowing the creation of the tables."""
import mysql.connector
from param import parameters

class Create():
    """Class creating the tables in the database."""
    def __init__(self):
        """Constructor"""
        self.conn = mysql.connector.connect(
        host=parameters["host"],
        user=parameters["user"],
        passwd=parameters["password"],
        database=parameters["database"])

    def construct(self):
        """Function constructing the database."""
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("CREATE TABLE Product (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
        name_product VARCHAR(100) NOT NULL, quantity VARCHAR(40) NOT NULL,\
        id_category SMALLINT NOT NULL, nutri_score CHAR(1) NOT NULL,\
        ingredients TEXT NOT NULL, link_url VARCHAR(200) NOT NULL, store VARCHAR(200), PRIMARY KEY (id));\
        \
        CREATE TABLE Favorite (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
        id_product_replaced SMALLINT NOT NULL, id_product_replacing SMALLINT NOT NULL,\
        date_creation_favorite DATETIME NOT NULL, PRIMARY KEY (id));\
        \
        CREATE TABLE Store (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
        name VARCHAR(100) NOT NULL, PRIMARY KEY (id));\
        \
        CREATE TABLE Category (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,\
        category_name VARCHAR(50) NOT NULL,PRIMARY KEY (id)); \
        \
        CREATE TABLE Stores_products (id_product SMALLINT UNSIGNED NOT NULL,\
        id_store SMALLINT UNSIGNED NOT NULL, PRIMARY KEY (id_product, id_store));", multi=True)

        # Iteration via json categories
        self.mycursor.execute("INSERT INTO Category (category_name) VALUES (%s);", (category,))
        self.conn.commit()


creation = Create()
creation.construct()
