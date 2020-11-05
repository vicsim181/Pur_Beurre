#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script feeding the tables, using the SQLAlchemy ORM."""
import json, requests
from ormcreation import Category, Product, Store, Junction
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

eng = create_engine('mysql://root:japon+71@#cclmvdf@localhost/essai', echo=True)
Session = sessionmaker(bind=eng)
ses = Session()

with open('./Scripts/settings.json', 'r', encoding="utf-8") as settings:
    data = json.load(settings)

categories = ses.query(Category)
j = 1
i = 1
junction = []
for category in categories:
    print (category.Id)
    url = f'''https://world.openfoodfacts.org/cgi/search.pl?search_terms={category}&search_simple=1&action=process&json=1&page={data['page']}&page_size={data['page_size']}'''
    json = requests.get(url).json()
    raw_products = json['products']
    for raw_product in raw_products:
        product = Product(name=raw_product['product_name'], quantity=raw_product['quantity'], id_category=category.Id,
            nutri_score=raw_product['nutriscore_grade'], ingredients=raw_product['ingredients_text_fr'], link_url=raw_product['url'])
        ses.add(product)
        if raw_product['stores_tags']:
            for store in raw_product['stores_tags']:
                pr = ses.query(Product).filter(Product.name==raw_product['product_name']).first()
                # id_pr = pr.Id
                jnct_st_pr = Junction(id_product=pr.Id, name_store=store, id_store=j)
                j += 1
                ses.add(jnct_st_pr)
        i += 1
ses.commit()

# pr = ses.query(Product).filter(Product.name==raw_product['product_name'])
#                 id_pr = pr.Id