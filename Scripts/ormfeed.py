#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script feeding the tables, using the SQLAlchemy ORM."""
import json
import requests
import sys
from sqlalchemy import and_, func
from sqlalchemy.orm import sessionmaker
sys.path.append("D:/Github/P5/github")
from Models.product import Product
from Models.category import Category
from Models.junction import StoreProduct
from Models.base import eng
from Models.store import Store


def main():
    """Initializing the session."""
    Session = sessionmaker(bind=eng)
    ses = Session()

    """Extracting some parameters from the settings.json file."""
    with open('../models/settings.json', 'r') as settings:
        data = json.load(settings)

    """Starting the extraction from the OpenFoodFacts API,\
    feeding the tables Product and Store with part of the data collected."""
    i = 1
    categories = ses.query(Category)
    for category in categories:
        url = f'''https://world.openfoodfacts.org/cgi/search.pl?search_terms={category.name}&search_simple=1&action=process&json=1&page={data['page']}&page_size={data['page_size']}'''
        js = requests.get(url).json()
        raw_products = js['products']
        for raw_product in raw_products:
            product = Product(name=raw_product['product_name'],
                              quantity=raw_product['quantity'],
                              id_category=category.Id,
                              nutri_score=raw_product['nutriscore_grade'],
                              ingredients=raw_product['ingredients_text_fr'],
                              link_url=raw_product['url'],
                              stores=str(raw_product['stores_tags']))
            ses.add(product)
            if raw_product['stores_tags']:
                for store in raw_product['stores_tags']:
                    store_add = Store(name=store)
                    ses.add(store_add)
            i += 1
    ses.commit()

    """Deleting the duplicates in the Store table."""
    subq = (
        ses.query(Store.name, func.min(Store.Id).label("min_id"))
        .group_by(Store.name)
    ) .subquery('name_min_id')
    duplicates_store = (ses.query(Store).join(subq,
                        and_(Store.name == subq.c.name,
                             Store.Id != subq.c.min_id)))
    for dup in duplicates_store:
        ses.delete(dup)
    ses.commit()

    """Cleaning the stores column of the Product table."""
    junction = []
    products = ses.query(Product)
    for product in products:
        if product.stores != '[]':
            detail = product.stores.split(',')
            for element in detail:
                element = element.replace("'", "").replace('[', '').replace(']', '').strip()
                stores = ses.query(Store).filter(Store.name == f'{element}').first()
                junction.append([product.Id, product.name, element, stores.Id])

    """Inserting the data in the junction table: Store_Product,\
    with only the Ids of the products and stores."""
    for line in junction:
        add_to_junction = StoreProduct(id_product=f'{line[0]}',
                                       id_store=f'{line[3]}')
        ses.add(add_to_junction)
    ses.commit()


if __name__ == "__main__":
    main()
