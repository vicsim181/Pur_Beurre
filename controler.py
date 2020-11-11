"""File holding the Controler Class,\
   managing the actions coming from the client."""
from views import View
from model import Model


class Controler():
    """Class holding the controler and its functions."""
    def __init__(self):
        self.view = View()
        self.model = Model()

    def display_main_menu(self):
        """Function displaying the Main Menu in the console line."""
        self.view.main_menu(lambda: print("Leaving\n\n\n"),
                            self.display_categories,
                            self.display_favorites,
                            "Select an action to perform: ", 2)

    def display_categories(self):
        """Function displaying the categories selection menu."""
        categories = self.model.get_categories()
        self.view.categories_menu(categories,
                                  lambda: print("Leaving\n\n\n"),
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
                                lambda: print("Leaving\n\n\n"),
                                self.save_product,
                                self.display_products,
                                self.display_main_menu,
                                "Please select an action: ")

    def save_product(self, product):
        self.model.save_product(product)
        # Renvoyer les 5 meilleures propositions de la catégorie.
        #view replacement_suggestion

    def display_favorites(self):
        favorites = self.model.get_favorites()
        self.view.favorites(favorites)


controler = Controler()
controler.display_main_menu()
