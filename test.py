import requests
# import json

PAGE = 1
PAGE_SIZE = 50
PRODUCT = 'saucisson sec'
url = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms={PRODUCT}&search_simple=1&action=process&json=1&page={PAGE}&page_size={PAGE_SIZE}'
json = requests.get(url).json()
raw_products = json['products']
products = []
for raw_product in raw_products:
    product = {'nutriscore' : raw_product["nutriscore_grade"], 'name' : raw_product["product_name"]}
    products.append(product)



print(products)