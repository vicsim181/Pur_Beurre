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

    def get_categories(self):
        self.categories = self.ses.query(Category)
        return self.categories

    def get_products(self, num_category, i):
        products = self.ses.query(Product).filter(
                   Product.id_category == num_category)
        category = self.ses.query(Category).filter(
                        Category.Id == num_category).first()
        if products[i].stores != '[]':
            stores_list = []
            stores = products[i].stores.split(',')
            for store in stores:
                store = store.replace('[', '').replace(']', '').replace("'", "")
                stores_list.append(store)
            str_stores = ''
            for store in stores_list:
                str_stores += str(store).title() + ' / '
        else:
            str_stores = "Not available in any store at the moment"
        return products[i], category.name, str_stores

    def save_product(self, product):
        pass

    def get_favorites(self):
        pass
