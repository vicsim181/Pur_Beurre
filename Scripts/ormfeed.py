#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script feeding the tables, using the SQLAlchemy ORM."""
import sys
sys.path.append('D:\Github\P5\github')
import json, requests
from models.product import Product
from models.favorite import Favorite
from models.category import Category
from models.junction import StoreProduct
from models.base import Base, eng
from models.store import Store
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# eng = create_engine('mysql://root:japon+71@#cclmvdf@localhost/essai')#, echo=True)
Session = sessionmaker(bind=eng)
ses = Session()

with open('../models/settings.json', 'r') as settings:
    data = json.load(settings)

i = 1
junction = []

categories = ses.query(Category)
for category in categories:
    url = f'''https://world.openfoodfacts.org/cgi/search.pl?search_terms={category.name}&search_simple=1&action=process&json=1&page={data['page']}&page_size={data['page_size']}'''
    json = requests.get(url).json()
    raw_products = json['products']
    for raw_product in raw_products:
        product = Product(name=raw_product['product_name'], quantity=raw_product['quantity'], id_category=category.Id,
        nutri_score=raw_product['nutriscore_grade'], ingredients=raw_product['ingredients_text_fr'], link_url=raw_product['url'], stores=str(raw_product['stores_tags']))
        ses.add(product)
        if raw_product['stores_tags']:
            for store in raw_product['stores_tags']:
                store_add = Store(name=store)
                ses.add(store_add)
        i += 1
ses.commit()

# pr = ses.query(Product).filter(Product.name==raw_product['product_name'])
#                 id_pr = pr.Id

# pr_name = raw_product['product_name']
#                 pr = ses.query(Product).filter(Product.name == f'{pr_name}').first()
#                 stor = ses.query(Store).filter(Store.name == f'{store}').first()
#                 jnct_st_pr = StoreProduct(id_product=pr.Id, name_product=(f'{pr_name}'), name_store=store, id_store=stor.Id)
#                 j += 2
#                 ses.add(jnct_st_pr)