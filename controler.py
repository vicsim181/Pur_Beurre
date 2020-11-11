"""File holding the Controler Class, managing the actions coming from the client."""
from views import View
from model import Model


class Controler():
    """Class holding the controler and its functions."""
    def __init__(self):
        self.view = View()
        self.model = Model()

    def display_main_menu(self):
        """Function displaying the Main Menu in the console line."""
        loop = True
        while loop:
            print("\n")
            self.view.display_main_menu()
            action = input("What's your choice?: ").lower()
            print("\n"
                  "\n"
                  "\n"
                  "\n")
            if action == "q":
                exit()
            elif action == "1":
                categories = self.model.get_categories()
                self.display_categories(categories)
            elif action == "2":
                self.view.display_favorites()
            else:
                self.view.display_wrong_decision()

    def display_categories(self, cats):
        """Function displaying the categories selection menu."""
        loop = True
        while loop:
            print("\n")
            self.view.display_categories_menu(cats)
            action = input("What's your choice?: ").lower()
            print("\n"
                  "\n"
                  "\n"
                  "\n")
            if action == "q":
                exit()
            elif action == "m":
                self.display_main_menu()
            elif action in ('1', '2', '3', '4', '5'):
                id_prod = 1
                self.display_products(action, id_prod)
            else:
                self.view.display_wrong_decision()

    def display_products(self, category, id_product):
        """Function displaying the products from the selected category."""
        loop = True
        while loop:
            product = self.model.get_products(category, id_product)
            print("\n")
            self.view.display_products_list(product)
            action = input("What's your choice?: ").lower()
            print("\n"
                  "\n"
                  "\n"
                  "\n")
            if action == "q":
                exit()
            elif action == "m":
                self.display_main_menu()
            elif action == '1':
                self.save_in_favorites()
            elif action == '2':
                self.display_products(category, id_product + 1)
            elif action == '0':
                if id_product == 1:
                    self.view.display_wrong_decision()
                else:
                    self.display_products(category, id_product + 1)
            else:
                self.view.display_wrong_decision()


controler = Controler()
controler.display_main_menu()