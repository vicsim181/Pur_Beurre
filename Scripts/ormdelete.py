"""File deleting the tables from the database."""
import sys
sys.path.append('D:/Github/P5/github')
from models.category import Category
from models.product import Product
from models.store import Store
from models.favorite import Favorite
from models.junction import StoreProduct
from models.base import eng


def main():
    for Table in (StoreProduct, Favorite, Store, Product, Category):
        Table.__table__.drop(eng)


if __name__ == "__main__":
    main()
