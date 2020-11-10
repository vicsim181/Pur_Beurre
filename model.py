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


