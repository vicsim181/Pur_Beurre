"""File holding the model Class providing the controler with the data as requested by the user."""
import sys
from datetime import datetime
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
    Session = sessionmaker(bind=eng)
    SES = Session()

    @staticmethod
    def get_categories():
        """Function gathering the categories from the database."""
        categories = Model.SES.query(Category)
        categ_names = [str(category.name) for category in categories]
        return categ_names

    @staticmethod
    def format_stores(stores_id):
        """Function formatting the stores names as Strings."""
        str_stores = ''
        for element in stores_id:
            stores_name = Model.SES.query(Store.name).filter(Store.Id == element).first()
            str_stores += str(stores_name).title() + ' '
        if str_stores == '':
            str_stores = "Not available in any store at the moment"
        str_stores = str_stores.replace('(', '').replace(')', '').replace("'", "")
        return str_stores

    @staticmethod
    def format_favorites():
        """Function ordering the favorites and their Id in the table."""
        nb = Model.SES.query(Favorite).order_by(Favorite.date_creation)
        for i, favorite in enumerate(nb):
            favorite.Id = i + 1

    @staticmethod
    def format_category(name_category):
        num_category = Model.SES.query(Category.Id).filter(Category.name == name_category).first()
        return num_category

    @staticmethod
    def get_products(num_category, i):
        """Function collecting the products in the chosen category."""
        products = Model.SES.query(Product).filter(Product.id_category == num_category)
        stores_id = Model.SES.query(StoreProduct.id_store).filter(StoreProduct.id_product == products[i].Id)
        str_stores = Model.format_stores(stores_id)
        max_cat = len(Model.SES.query(Product).filter(Product.id_category == num_category).all())
        return products[i], str_stores, max_cat

    @staticmethod
    def looking_for_suggestion(id_prod, id_cat, grade):
        """Function looking for the suggestions in the chosen category."""
        results = Model.SES.query(Product).filter(Product.id_category == id_cat, Product.nutri_score == grade)
        nb = []
        for element in results:
            nb.append(element.Id)
        if id_prod in nb:
            nb.remove(id_prod)
        return nb

    @staticmethod
    def generate_suggestions(id_prod, id_cat):
        """Function formating and generating the chosen suggestions."""
        nutri = ['a', 'b', 'c', 'd', 'e']
        suggestions = []
        i = 0
        while len(suggestions) < 5:
            results = Model.looking_for_suggestion(id_prod, id_cat, nutri[0 + i])
            for element in results:
                suggestions.append(element)
            i += 1
        str_stores = []
        for i in range(0, 5):
            suggestions += Model.SES.query(Product).filter(Product.Id == suggestions[i])
            id_stores = Model.SES.query(StoreProduct.id_store).filter(StoreProduct.id_product == suggestions[i])
            str_stores.append(Model.format_stores(id_stores))
        return suggestions[-5:], str_stores

    @staticmethod
    def replace(product_replaced, id_replacing):
        """Function saving a product replacement in the favorite table."""
        nb = len(Model.SES.query(Favorite).all())
        favorite = Favorite(Id=nb + 1, Id_product_replaced=product_replaced.Id, Id_product_replacing=id_replacing,
                            date_creation=datetime.now())
        try:
            Model.SES.add(favorite)
            Model.SES.commit()
            return 'ok'
        except IntegrityError:  # Here to manage the error when intenting to save a replacement already saved
            Model.SES.rollback()
            return 'nok'

    @staticmethod
    def get_favorites():
        """Function collecting the favorites in the favorite table."""
        favorites = Model.SES.query(Favorite).order_by(Favorite.date_creation)
        list_favorites = []
        for line in favorites:
            replaced = Model.SES.query(Product.name).filter(Product.Id == line.Id_product_replaced).first()
            replacing = Model.SES.query(Product.name).filter(Product.Id == line.Id_product_replacing).first()
            replaced = str(replaced).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace(
                                                                                                         '"', '')
            replacing = str(replacing).replace('(', '').replace(')', '').replace(',', '').replace("'", "").replace(
                                                                                                           '"', '')
            date = str(line.date_creation)
            list_favorites.append([replaced, replacing, date])
        return list_favorites

    @staticmethod
    def delete_all_favorites():
        """Function deleting all the rows of the favorite table."""
        Model.SES.query(Favorite).delete()
        Model.SES.commit()

    @staticmethod
    def delete_favorites(choice):
        """Function deleting the selected row of the favorite table."""
        Model.SES.query(Favorite).filter(Favorite.Id == choice).delete()
        Model.format_favorites()
        Model.SES.commit()
