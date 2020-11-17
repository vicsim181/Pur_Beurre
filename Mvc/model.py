"""File holding the model Class providing the controler\
   with the data as requested by the user."""
import sys
from datetime import datetime
# from sqlalchemy import and_, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
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
        """Function gathering the categories from the database."""
        self.categories = self.ses.query(Category)
        return self.categories

    def format_stores(self, stores_id):
        """Function formatting the stores names as Strings."""
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

    def format_favorites(self):
        """Function ordering the favorites and their Id in the table."""
        nb = self.ses.query(Favorite).order_by(Favorite.date_creation)
        for i, favorite in enumerate(nb):
            favorite.Id = i + 1

    def get_products(self, num_category, i):
        """Function collecting the products in the chosen category."""
        products = self.ses.query(Product).filter(
                   Product.id_category == num_category)
        category = self.ses.query(Category).filter(
                        Category.Id == num_category).first()
        stores_id = self.ses.query(StoreProduct.id_store).filter(
                    StoreProduct.id_product == products[i].Id)
        str_stores = self.format_stores(stores_id)
        max_cat = len(self.ses.query(Product).filter(
                   Product.id_category == num_category).all())
        return products[i], category.name, str_stores, max_cat

    def looking_for_suggestion(self, id_prod, id_cat, grade):
        """Function looking for the suggestions in the chosen category."""
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
        """Function formating and generating the chosen suggestions."""
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
        """Function saving a product replacement in the favorite table."""
        nb = len(self.ses.query(Favorite).all())
        favorite = Favorite(Id=nb + 1,
                            Id_product_replaced=product_replaced.Id,
                            Id_product_replacing=id_replacing,
                            date_creation=datetime.now())
        try:
            self.ses.add(favorite)
            self.ses.commit()
            return 'ok'
        except IntegrityError:  # Here to manage the error when intenting to save a replacement already saved in the table.
            self.ses.rollback()
            return 'nok'

    def get_favorites(self):
        """Function collecting the favorites in the favorite table."""
        favorites = self.ses.query(Favorite).order_by(Favorite.date_creation)
        list_favorites = []
        for line in favorites:
            replaced = self.ses.query(Product.name).filter(
                       Product.Id == line.Id_product_replaced).first()
            replacing = self.ses.query(Product.name).filter(
                        Product.Id == line.Id_product_replacing).first()
            replaced = str(replaced).replace('(', '').replace(')', '').replace(
                           ',', '').replace("'", "").replace('"', '')
            replacing = str(replacing).replace('(', '').replace(
                            ')', '').replace(',', '').replace("'", "").replace(
                            '"', '')
            date = str(line.date_creation)
            list_favorites.append([replaced, replacing, date])
        return list_favorites

    def delete_all_favorites(self):
        """Function deleting all the rows of the favorite table."""
        self.ses.query(Favorite).delete()
        self.ses.commit()

    def delete_favorites(self, choice):
        """Function deleting the selected row of the favorite table."""
        self.ses.query(Favorite).filter(Favorite.Id == choice).delete()
        self.format_favorites()
        self.ses.commit()
