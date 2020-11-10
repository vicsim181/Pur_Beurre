"""Script holding the view class,managing the different views of the application."""


class View():
    """Class holding the views"""

    def __init__(self):
        pass

    def display_main_menu(self):
        """Function allowing the View to display the home menu."""
        print("#################################################################\n"
              "#####################       MAIN MENU       #####################\n"
              "###########        Select an action to perform        ###########\n"
              "#                                                               #\n"
              "#                1. Replace a product                           #\n"
              "#                2. Consult my favorites                        #\n"
              "#                                                               #\n"
              "#_______________________________________________________________#\n"
              "#                 Press the number of your choice               #\n"
              "#                       Press Q to close                        #\n")

    def display_categories_menu(self, cat):
        """Function allowing the client to choose a category."""
        print("#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########       Select a category of products      ############\n"
              "#                                                               #\n")
        for i, element in enumerate(cat):
            print(f"      {i + 1}: {element.name.title()}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press the number of your choice               #\n"
              "#                Press M to go back to Main Menu                #\n")

    def display_products_list(self, products):
        """Function displaying the products of the selected category."""
        print("#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########             Select a product              ###########\n"
              "#                                                               #\n")
        for element in products:
            print(f" -Name: {element.name.title()}\n"
                  f" -Quantity: {element.quantity}\n"
                  f" -Ingredients: {element.ingredients}\n"
                  f" -Nutriscore: {element.nutriscore}\n"
                  f" -URL: {element.url}\n"
                  f" -Store(s): {element.stores}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press 1 to select this product                #\n"
              "#              To display the next product press 2              #\n"
              "#          To go back to the previous product press 0           #\n"
              "#                Press M to go back to Main Menu                #\n")

    def display_favorites(self, favorites):
        """Function displaying the favorite of the user."""
        print("#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########             Select a product              ###########\n"
              "#                                                               #\n")
        for index, element in enumerate(favorites):
            print(f""" {index + 1}- "{element[index][0]}" replaced by \
                     "{element[index][1]}" \n""")
        print("#_______________________________________________________________#\n"
              "#              Press D to delete all the favorites              #\n"
              "#                Press M to go back to Main Menu                #\n")

    def display_wrong_decision(self):
        """Function displaying the message in case of a wrong selection."""
        print("#################################################################\n"
              "                  PLEASE ENTER A CORRECT VALUE                   \n"
              "#################################################################\n")
