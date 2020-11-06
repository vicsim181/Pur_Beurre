"""File creating the tables in the database."""
import sys
sys.path.append('D:/Github/P5/github')
from models.base import Base, eng
from models.category import Category
from models.product import Product
from models.favorite import Favorite
from models.junction import StoreProduct
from models.store import Store

Base.metadata.create_all(eng)
