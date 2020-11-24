"""File deleting the tables from the database."""
import sys
sys.path.append('..')
from Models.category import Category
from Models.product import Product
from Models.store import Store
from Models.favorite import Favorite
from Models.junction import StoreProduct
from Models.base import eng


def main():
    for Table in (StoreProduct, Favorite, Store, Product, Category):
        Table.__table__.drop(eng)


if __name__ == "__main__":
    main()
