"""Script holding the view class,managing the different views of the application."""
from utils import int_input


class View():
    """Class holding the views"""

    def __init__(self):
        pass

    def main_menu(self, alt_callback, callback, callback_2,
                  message, nb_choices):
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
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, nb_choices, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback()
        else:
            callback_2()

    def categories_menu(self, categories, alt_callback, callback_1, callback_2,
                        message):
        """Function allowing the client to choose a category."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########       Select a category of products      ############\n"
              "#                                                               #\n")
        for i, element in enumerate(categories):
            print(f"      {i + 1}: {element.name.title()}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press the number of your choice               #\n"
              f"#                Press {i + 2} to go back to Main Menu                #\n"
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, (i + 1), message)
        if choice == 0:
            alt_callback()
        elif choice in range(1, i+2):
            callback_1(choice, 0)
        else:
            callback_2()

    def products_list(self, category_name, category_id, product, i, stores,
                      alt_callback, callback, callback_2, callback_3, message):
        """Function displaying the products of the selected category."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              f"                            {category_name}\n"
              "###########             Select a product              ###########\n"
              f"#                          Product n°{i + 1}                          #\n")
        print(f" -Name: {product.name}\n"
              f" -Quantity: {product.quantity}\n"
              f" -Nutriscore: {product.nutri_score}\n"
              f" -Ingredients: {product.ingredients}\n"
              f" -URL: {product.link_url}\n"
              f" -Store(s): {stores}\n")
        print("#_______________________________________________________________#\n"
              "#                 Press 1 to select this product                #\n"
              "#              To display the next product press 2              #\n"
              "#          To go back to the previous product press 3           #\n"
              "#                Press 4 to go back to Main Menu                #\n"
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, 4, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback(product)
        elif choice == 2:
            callback_2(category_id,
                       i + 1)
        elif choice == 3:
            if i == 0:
                callback_2(category_id,
                           i)
            else:
                callback_2(category_id,
                           i - 1)
        else:
            callback_3()

    def favorites(self, favorites):
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
              "#              Press 1 to delete all the favorites              #\n"
              "#                Press 2 to go back to Main Menu                #\n"
              "#                       Press 0 to close                        #\n")

    def wrong_decision(self):
        """Function displaying the message in case of a wrong selection."""
        print("\n"
              "\n"
              "\n"
              "#################################################################\n"
              "                  PLEASE ENTER A CORRECT VALUE                   \n"
              "#################################################################\n")

    def replacement_suggestion(self):
        pass

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
