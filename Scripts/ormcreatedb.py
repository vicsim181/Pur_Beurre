from base import Base, eng

from category import Category
from product import Product
from favorite import Favorite
from junction import StoreProduct
from store import Store

Base.metadata.create_all(eng)