"""Script holding the view class,managing the different views of the application."""
from utils import int_input


class View():
    """Class holding the views"""

    def __init__(self):
        pass

    def display_main_menu(self):
        """Function allowing the View to display the home menu."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
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
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########       Select a category of products      ############\n"
              "#                                                               #\n")
        for i, element in enumerate(cat):
            print(f"      {i + 1}: {element.name.title()}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press the number of your choice               #\n"
              "#                Press M to go back to Main Menu                #\n"
              "#                       Press Q to close                        #\n")

    def display_products_list(self, product):
        """Function displaying the products of the selected category."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########             Select a product              ###########\n"
              "#                                                               #\n")
        for element in product:
            print(f" -Name: {element[0].title()}\n"
                  f" -Quantity: {element[1]}\n"
                  f" -Nutriscore: {element[2]}\n"
                  f" -Ingredients: {element[3]}\n"
                  f" -URL: {element[4]}\n"
                  f" -Store(s): {element[5]}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press 1 to select this product                #\n"
              "#              To display the next product press 2              #\n"
              "#          To go back to the previous product press 0           #\n"
              "#                Press M to go back to Main Menu                #\n"
              "#                       Press Q to close                        #\n")

    def display_favorites(self, favorites):
        """Function displaying the favorite of the user."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "#####################       FAVORITES       #####################\n"
              "###########           Consult your favorite           ###########\n"
              "#                                                               #\n")
        for index, element in enumerate(favorites):
            print(f""" {index + 1}- "{element[index][0]}" replaced by \
                     "{element[index][1]}" \n""")
        print("#_______________________________________________________________#\n"
              "#              Press D to delete all the favorites              #\n"
              "#                Press M to go back to Main Menu                #\n")

    def display_wrong_decision(self):
        """Function displaying the message in case of a wrong selection."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "                  PLEASE ENTER A CORRECT VALUE                   \n"
              "#################################################################\n")

    def input_user(self, alt_callback, callback, message, nb_choices):
        choice = int_input(0, nb_choices, message)
        if choice == 0:
            alt_callback()
        else:
            callback(choice)

    def foo_1(self):
        print("Leaving ")

    def foo_2(self, choice):
        print('Your choice is :', choice)


def foo_3(choice, x):
    print('Your choice is :', choice, ' ', x)

# view = View()
# view.input_user(view.foo_1, lambda choice: foo_3(choice, 'canard'), 'Veuillez choisir un produit: ', 5)
