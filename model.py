"""File holding the model Class providing the controler\
   with the data as requested by the user."""
import sys
from datetime import datetime
# from sqlalchemy import and_, func
from sqlalchemy.orm import sessionmaker
sys.path.append("D:/Github/P5/github")
from Models.product import Product
from Models.category import Category
from Models.junction import StoreProduct
from Models.favorite import Favorite
from Models.base import eng
from Models.store import Store


class Model():
    """Class holding the model and its functions."""
    def __init__(self):
        Session = sessionmaker(bind=eng)
        self.ses = Session()

    def get_categories(self):
        self.categories = self.ses.query(Category)
        return self.categories

    def format_stores(self, stores_id):
        str_stores = ''
        for element in stores_id:
            stores_name = self.ses.query(Store.name).filter(
                          Store.Id == element).first()
            str_stores += str(stores_name).title() + ' '
        if str_stores == '':
            str_stores = "Not available in any store at the moment"
        str_stores = str_stores.replace('(', '').replace(')', '').replace("'",
                                                                          "")
        return str_stores

    def get_products(self, num_category, i):
        products = self.ses.query(Product).filter(
                   Product.id_category == num_category)
        category = self.ses.query(Category).filter(
                        Category.Id == num_category).first()
        stores_id = self.ses.query(StoreProduct.id_store).filter(
                    StoreProduct.id_product == products[i].Id)
        str_stores = self.format_stores(stores_id)
        return products[i], category.name, str_stores

    def looking_for_suggestion(self, id_prod, id_cat, grade):
        results = self.ses.query(Product).filter(
                   Product.id_category == id_cat,
                   Product.nutri_score == grade)
        nb = []
        for element in results:
            nb.append(element.Id)
        if id_prod in nb:
            nb.remove(id_prod)
        return nb

    def generate_suggestions(self, id_prod, id_cat):
        nutri = ['a', 'b', 'c', 'd', 'e']
        suggestions = []
        i = 0
        while len(suggestions) < 5:
            results = self.looking_for_suggestion(id_prod, id_cat,
                                                  nutri[0 + i])
            for element in results:
                suggestions.append(element)
            i += 1
        str_stores = []
        for i in range(0, 5):
            suggestions += self.ses.query(Product).filter(
                           Product.Id == suggestions[i])
            id_stores = self.ses.query(StoreProduct.id_store).filter(
                        StoreProduct.id_product == suggestions[i])
            str_stores.append(self.format_stores(id_stores))
        return suggestions[-5:], str_stores

    def replace(self, product_replaced, id_replacing):
        favorite = Favorite(Id_product_replaced=product_replaced.Id,
                            Id_product_replacing=id_replacing,
                            date_creation=datetime.now())
        self.ses.add(favorite)
        self.ses.commit()

    def get_favorites(self):
        favorites = self.ses.query(Favorite)
        list_favorites = []
        for line in favorites:
            replaced = self.ses.query(Product.name).filter(
                       Product.Id == line.Id_product_replaced).first()
            replacing = self.ses.query(Product.name).filter(
                        Product.Id == line.Id_product_replacing).first()
            replaced = str(replaced).replace('(', '').replace(')', '').replace(
                           ',', '').replace("'", "").replace('"','')
            replacing = str(replacing).replace('(', '').replace(')',
                            '').replace(',', '').replace("'", "").replace(
                            '"', '')
            date = str(line.date_creation)
            list_favorites.append([replaced, replacing, date])
        return list_favorites

    def delete_favorites(self):
        self.ses.query(Favorite).delete()
        self.ses.commit()
