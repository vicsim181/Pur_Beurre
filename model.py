"""File holding the model Class providing the controler with the data as requested by the user."""
import sys
from sqlalchemy import and_, func
from sqlalchemy.orm import sessionmaker
sys.path.append("D:/Github/P5/github")
from Models.product import Product
from Models.category import Category
from Models.junction import StoreProduct
from Models.base import eng
from Models.store import Store


class Model():
    """Class holding the model and its functions."""
    def __init__(self):
        Session = sessionmaker(bind=eng)
        self.ses = Session()

    def format_stores(self, input_stores):
        list_stores = []
        stores = input_stores.split(',')
        for store in stores:
            store = store.replace("'", "").replace('[', '').replace(']', '').strip()
            list_stores.append(store)
        return list_stores

    def get_categories(self):
        self.categories = self.ses.query(Category)
        return self.categories

    def get_products(self, num_category, id_prod):
        products = self.ses.query(Product).filter(
                    Product.id_category == num_category,
                    Product.Id == id_prod)  #TROUVER ID PRODUIT DU DEBUT DE LA CATEGORIE
        for product in self.request:
            if product.stores != '[]':
                stores = self.format_stores(product.stores)
            else:
                stores = "Not available in any store at the moment"
            products.append([product.name,
                             product.quantity,
                             product.nutri_score,
                             product.ingredients,
                             product.link_url,
                             stores])
        return products
