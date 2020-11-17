"""Script holding the view class,\
   managing the different views of the application."""
from utils import int_input


class View():
    """Class holding the views"""

    def __init__(self):
        pass

    def main_menu(self, alt_callback, callback, callback_2,
                  message):
        """Function allowing the View to display the home menu."""
        print("\n\n\n\n\n\n\n\n\n"
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
        choice = int_input(0, 2, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback()
        else:
            callback_2()

    def categories_menu(self, categories, alt_callback, callback_1, callback_2,
                        message):
        """Function allowing the client to choose a category."""
        print("\n\n\n\n\n\n\n\n\n"
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
        choice = int_input(0, (i + 2), message)
        if choice == 0:
            alt_callback()
        elif choice in range(1, i+2):
            callback_1(choice, 0)
        else:
            callback_2()

    def products_list(self, category_name, category_id, product, i, stores,
                      alt_callback, callback, callback_2, callback_3, message,
                      max_cat):
        """Function displaying the products of the selected category."""
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              f"                            {category_name}\n"
              "###########             Select a product              ###########\n"
              f"#                         Product n°{i + 1} / {max_cat}                      #\n")
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
            if i+1 == max_cat:
                callback_2(category_id,
                           i)
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

    def suggestions(self, suggestion, stores, i, alt_callback, callback,
                    callback_2, callback_3, message):
        """Function displaying the propositions to replace a selected product."""
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################  REPLACING A PRODUCT  #####################\n"
              "###########       Select the alternative product     ############\n"
              f"#                        Product n°{i + 1} / 5                        #\n")
        print(f" -Name: {suggestion[i].name}\n"
              f" -Quantity: {suggestion[i].quantity}\n"
              f" -Nutriscore: {suggestion[i].nutri_score}\n"
              f" -Ingredients: {suggestion[i].ingredients}\n"
              f" -URL: {suggestion[i].link_url}\n"
              f" -Store(s): {stores[i]}\n")
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
            callback(suggestion[i])
        elif choice == 2:
            if i == 4:
                callback_2(suggestion, stores, i, alt_callback, callback,
                           callback_2, callback_3, message)
            callback_2(suggestion, stores, i + 1, alt_callback, callback,
                       callback_2, callback_3, message)
        elif choice == 3:
            if i == 0:
                callback_2(suggestion, stores, i, alt_callback, callback,
                           callback_2, callback_3, message)
            else:
                callback_2(suggestion, stores, i - 1, alt_callback, callback,
                           callback_2, callback_3, message)
        else:
            callback_3()

    def replacement(self, alt_callback, callback, message):
        """Function displaying the confirmation message\
           that the product is replaced."""
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################      Replacement      #####################\n"
              "#                                                               #\n"
              "#                   Your replacement is saved!                  #\n"
              "#                                                               #\n"
              "#_______________________________________________________________#\n"
              "#                 Press 1 to go back to Main Menu               #\n"
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()

    def favorites(self, favorites, alt_callback, callback, callback_2, message):
        """Function displaying the favorite of the user."""
        try:
            print("\n\n\n\n\n\n\n\n\n"
                  "#################################################################\n"
                  "#####################       FAVORITES       #####################\n"
                  "###########          Consult your favorite(s)         ###########\n"
                  "#                                                               #\n")
            for i, element in enumerate(favorites):
                print(f""" {i + 1}- | {element[0]} | replaced by | {element[1]} | on | {element[2]} |\n""")
            print("#_______________________________________________________________#\n"
                  f"#           !!! Press {i + 3} to delete all the favorites !!!         #\n"
                  "#         To delete a particular line, press its number         #\n"
                  f"#                Press {i + 2} to go back to Main Menu                #\n"
                  "#                       Press 0 to close                        #\n")
            choice = int_input(0, i + 3, message)
            if choice == 0:
                alt_callback()
            elif choice in range(1, i + 2):
                callback(choice)
            elif choice == (i + 3):
                callback('all')
            else:
                callback_2()
        except UnboundLocalError:
            print("#                                                               #\n"
                  "#                   No favorite for the moment                  #\n"
                  "#_______________________________________________________________#\n"
                  "#                Press 1 to go back to Main Menu                #\n"
                  "#                       Press 0 to close                        #\n")
            choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback_2()

    def favorite_error(self, alt_callback, callback, message):
        """Function warning the user that the attempted replacement has already\
           been done before."""
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################       Favorites       #####################\n"
              "#                                                               #\n"
              "#              !!!THIS REPLACEMENT HAS ALREADY BEEN             #\n"
              "#                   ADDED TO YOUR FAVORITES!!!                  #\n"
              "#_______________________________________________________________#\n"
              "#                 Press 1 to go back to Main Menu               #\n"
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()

    def delete_favorites(self, alt_callback, callback, message):
        """Function displaying the confirmation message\
           that the product is replaced."""
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################       Favorites       #####################\n"
              "#                                                               #\n"
              "#                   Your favorites are deleted!                 #\n"
              "#                                                               #\n"
              "#_______________________________________________________________#\n"
              "#                 Press 1 to go back to Main Menu               #\n"
              "#                       Press 0 to close                        #\n")
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()
