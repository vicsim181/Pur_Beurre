"""File creating the tables in the database."""
import sys
sys.path.append('..')
from Models.base import Base, eng
from Models.category import Category
from Models.product import Product
from Models.favorite import Favorite
from Models.junction import StoreProduct
from Models.store import Store

Base.metadata.create_all(eng)
