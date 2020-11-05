from models.category import Category
from models.product import Product
from models.store import Store
from models.favorite import Favorite
from models.junction import StoreProduct
from models.base import eng


def main():
    for Table in (Favorite, Store, StoreProduct, Product, Category):
        Table.__table__.drop(eng)


if __name__ == "__main__":
    main()
