"""File holding the Controler Class,\
   managing the actions coming from the client."""
from views import View
from model import Model
from utils import leaving


class Controler():
    """Class holding the controler and its functions."""
    def __init__(self):
        self.view = View()
        self.model = Model()

    def display_main_menu(self):
        """Function displaying the Main Menu in the console line."""
        self.view.main_menu(leaving,
                            self.display_categories,
                            self.display_favorites,
                            "Select an action to perform: ")

    def display_categories(self):
        """Function displaying the categories selection menu."""
        categories = self.model.get_categories()
        self.view.categories_menu(categories,
                                  leaving,
                                  self.display_products,
                                  self.display_main_menu,
                                  "Please select a Category \
by entering its number: ")

    def display_products(self, category_id, i):
        """Function displaying the products from the selected category."""
        product, category_name, stores = self.model.get_products(category_id,
                                                                 i)
        self.view.products_list(category_name.title(), category_id,
                                product, i, str(stores),
                                leaving,
                                self.save_product,
                                self.display_products,
                                self.display_main_menu,
                                "Please select an action: ")

    def save_product(self, product):
        self.replaced_product = product
        self.replacement_suggestion(product.Id, product.id_category)

    def replacement_suggestion(self, product_id, id_category):
        suggestion, stores = self.model.generate_suggestions(product_id,
                                                             id_category)
        self.view.suggestions(suggestion, stores, 0,
                              leaving,
                              self.display_replacement, self.view.suggestions,
                              self.display_main_menu,
                              "Please select an action: ")

    def display_replacement(self, suggestion):
        self.model.replace(self.replaced_product, suggestion.Id)
        self.view.replacement(leaving, self.display_main_menu,
                              "Please select an action: ")

    def display_favorites(self):
        favorites = self.model.get_favorites()
        print(favorites)
        # self.view.favorites(favorites, leaving,
        #                     self.display_delete_favorites,
        #                     self.display_main_menu,
        #                     'Please select an action: ')

    def display_delete_favorites(self):
        pass


controler = Controler()
controler.display_main_menu()
