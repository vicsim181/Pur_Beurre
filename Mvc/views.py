"""Script holding different classes managing the different views of the application."""
from Mvc.utils import int_input


class View():
    """Generic mclass hosting generic functions or tools used by the other classes."""
    def print_header(name, action):
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################{:^22}".format(name), "#####################\n"
              "###########{:^42}".format(action), "###########\n"
              "#                                                               #")

    def print_middle(*args):
        for i, arg in enumerate(args):
            argument = str(i + 1) + "- " + arg
            print("#                   {:<43}".format(argument), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")

    def print_bottom(*args):
        for arg in args:
            print("#{:^62}".format(arg), "#")

    def print_product(subtitle, product, stores):
        print("#{:^62}".format(subtitle), "#\n")
        print(f" -Name: {product.name}\n"
              f" -Quantity: {product.quantity}\n"
              f" -Nutriscore: {product.nutri_score}\n"
              f" -Ingredients: {product.ingredients}\n"
              f" -URL: {product.link_url}\n"
              f" -Store(s): {stores}\n")
        print("#                                                               #\n"
              "#_______________________________________________________________#")


class Main():
    """Class holding the view of the main menu"""
    def display_view(alt_callback, callback, callback_2, message, header_title, header_sub):
        View.print_header(header_title, header_sub)
        View.print_middle("Replace a product", "Consult my favorites")
        View.print_bottom("Press the number of your choice", "Press 0 to close")
        choice = int_input(0, 2, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback()
        else:
            callback_2()


class Category():
    """Class holding the view of the categories menu"""
    def display_categories(categories, alt_callback, callback, callback_2, message, header_title, header_sub):
        View.print_header(header_title, header_sub)
        for i, category in enumerate(categories):
            argument = str(i + 1) + "- " + category.title()
            print("#                   {:<43}".format(argument), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")
        View.print_bottom("Press the number of your choice", f"Press {i+2} to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, (i + 2), message)
        if choice == 0:
            alt_callback()
        elif choice in range(1, i+2):
            callback(choice, 0)
        else:
            callback_2()


class Product():
    """Class holding the view of the different products menus"""
    def display_products(category_name, category_id, product, i, stores, alt_callback, callback, callback_2,
                         callback_3, replaced_product, message, max_products, header_title, header_sub):
        View.print_header(header_title, header_sub)
        subtitle = f"Product n°{str(i + 1)} / {str(max_products)}"
        View.print_product(subtitle, product, stores)
        View.print_bottom("Press 1 to select this product", "To display the next product press 2",
                          "To go back to the previous product press 3", "Press 4 to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, 4, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback(product, category_id, category_name)
        elif choice == 2:
            if i+1 == max_products:
                callback_2(category_id, i)
            callback_2(category_id, i + 1)
        elif choice == 3:
            if i == 0:
                callback_2(category_id, i)
            else:
                callback_2(category_id, i - 1)
        else:
            callback_3()

    def display_suggestions(product, i, stores, alt_callback, callback, callback_2, callback_3, replaced_product,
                            message, max_alter, header_title, header_sub):
        View.print_header(header_title, header_sub)
        subtitle = f"Product n°{str(i + 1)} / {str(max_alter)}"
        View.print_product(subtitle, product[i], stores)
        View.print_bottom("Press 1 to select this product", "To display the next product press 2",
                          "To go back to the previous product press 3", "Press 4 to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, 4, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback(product[i], replaced_product)
        elif choice == 2:
            if i+1 == max_alter:
                callback_2(product, i, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
            callback_2(product, i + 1, stores, alt_callback, callback, callback_2, callback_3,
                       replaced_product, message, 5, header_title, header_sub)
        elif choice == 3:
            if i == 0:
                callback_2(product, i, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
            else:
                callback_2(product, i - 1, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
        else:
            callback_3()


class Favorite():
    """Class holding the different views of the favorite"""
    def save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2, message):
        View.print_header(header_title, header_sub)
        print("#{:^62}".format(middle_message_1), "#\n"
              "#{:^62}".format(middle_message_2), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")
        View.print_bottom("Press 1 to go back to Main Menu", "Press 0 to close")
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()

    def save_successful(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2, message):
        Favorite.save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                              message)

    def save_unsuccessful(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                          message):
        Favorite.save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                              message)

    def consult(favorites, alt_callback, callback, callback_2, header_title, header_sub, message):
        try:
            View.print_header(header_title, header_sub)
            print("\n")
            for i, favorite in enumerate(favorites):
                argument = str(i + 1) + "- " + favorite[0] + " | replaced by | " + favorite[1] + " | on | " + favorite[2]
                print("{:<62}".format(argument))
            print("\n"
                  "#_______________________________________________________________#")
            View.print_bottom("To delete a particular line, press its number", f"Press {i + 3} to delete all the favorites",
                              f"To go back to Main Menu press {i + 2}", "Press 0 to close")
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
                  View.print_bottom("Press 1 to go back to Main Menu", "Press 0 to close")
            choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback_2()

    def delete_all(header_title, header_sub, middle_message, bottom_1, bottom_2, message, alt_callback, callback):
        View.print_header(header_title, header_sub)
        View.print_middle(middle_message)
        View.print_bottom(bottom_1, bottom_2)
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()



    # def main_menu(self, alt_callback, callback, callback_2,
    #               message):
    #     """Function allowing the View to display the home menu."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################       MAIN MENU       #####################\n"
    #           "###########        Select an action to perform        ###########\n"
    #           "#                                                               #\n"
    #           "#                1. Replace a product                           #\n"
    #           "#                2. Consult my favorites                        #\n"
    #           "#                                                               #\n"
    #           "#_______________________________________________________________#\n"
    #           "#                 Press the number of your choice               #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 2, message)
    #     if choice == 0:
    #         alt_callback()
    #     elif choice == 1:
    #         callback()
    #     else:
    #         callback_2()

    # def categories_menu(self, categories, alt_callback, callback_1, callback_2,
    #                     message):
    #     """Function allowing the client to choose a category."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################  REPLACING A PRODUCT  #####################\n"
    #           "###########       Select a category of products      ############\n"
    #           "#                                                               #\n")
    #     for i, element in enumerate(categories):
    #         print(f"      {i + 1}: {element.name.title()}\n")
    #     print("#_______________________________________________________________#\n"
    #           "#                 Press the number of your choice               #\n"
    #           f"#                Press {i + 2} to go back to Main Menu                #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, (i + 2), message)
    #     if choice == 0:
    #         alt_callback()
    #     elif choice in range(1, i+2):
    #         callback_1(choice, 0)
    #     else:
    #         callback_2()

    # def products_list(self, category_name, category_id, product, i, stores,
    #                   alt_callback, callback, callback_2, callback_3, message,
    #                   max_cat):
    #     """Function displaying the products of the selected category."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################  REPLACING A PRODUCT  #####################\n"
    #           f"                            {category_name}\n"
    #           "###########             Select a product              ###########\n"
    #           f"#                         Product n°{i + 1} / {max_cat}                      #\n")
    #     print(f" -Name: {product.name}\n"
    #           f" -Quantity: {product.quantity}\n"
    #           f" -Nutriscore: {product.nutri_score}\n"
    #           f" -Ingredients: {product.ingredients}\n"
    #           f" -URL: {product.link_url}\n"
    #           f" -Store(s): {stores}\n")
    #     print("#_______________________________________________________________#\n"
    #           "#                 Press 1 to select this product                #\n"
    #           "#              To display the next product press 2              #\n"
    #           "#          To go back to the previous product press 3           #\n"
    #           "#                Press 4 to go back to Main Menu                #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 4, message)
    #     if choice == 0:
    #         alt_callback()
    #     elif choice == 1:
    #         callback(product)
    #     elif choice == 2:
    #         if i+1 == max_cat:
    #             callback_2(category_id,
    #                        i)
    #         callback_2(category_id,
    #                    i + 1)
    #     elif choice == 3:
    #         if i == 0:
    #             callback_2(category_id,
    #                        i)
    #         else:
    #             callback_2(category_id,
    #                        i - 1)
    #     else:
    #         callback_3()

    # def suggestions(self, suggestion, stores, i, alt_callback, callback,
    #                 callback_2, callback_3, message):
    #     """Function displaying the propositions to replace a selected product."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################  REPLACING A PRODUCT  #####################\n"
    #           "###########       Select the alternative product     ############\n"
    #           f"#                        Product n°{i + 1} / 5                        #\n")
    #     print(f" -Name: {suggestion[i].name}\n"
    #           f" -Quantity: {suggestion[i].quantity}\n"
    #           f" -Nutriscore: {suggestion[i].nutri_score}\n"
    #           f" -Ingredients: {suggestion[i].ingredients}\n"
    #           f" -URL: {suggestion[i].link_url}\n"
    #           f" -Store(s): {stores[i]}\n")
    #     print("#_______________________________________________________________#\n"
    #           "#                 Press 1 to select this product                #\n"
    #           "#              To display the next product press 2              #\n"
    #           "#          To go back to the previous product press 3           #\n"
    #           "#                Press 4 to go back to Main Menu                #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 4, message)
    #     if choice == 0:
    #         alt_callback()
    #     elif choice == 1:
    #         callback(suggestion[i])
    #     elif choice == 2:
    #         if i == 4:
    #             callback_2(suggestion, stores, i, alt_callback, callback,
    #                        callback_2, callback_3, message)
    #         callback_2(suggestion, stores, i + 1, alt_callback, callback,
    #                    callback_2, callback_3, message)
    #     elif choice == 3:
    #         if i == 0:
    #             callback_2(suggestion, stores, i, alt_callback, callback,
    #                        callback_2, callback_3, message)
    #         else:
    #             callback_2(suggestion, stores, i - 1, alt_callback, callback,
    #                        callback_2, callback_3, message)
    #     else:
    #         callback_3()

    # def replacement(self, alt_callback, callback, message):
    #     """Function displaying the confirmation message\
    #        that the product is replaced."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################      Replacement      #####################\n"
    #           "#                                                               #\n"
    #           "#                   Your replacement is saved!                  #\n"
    #           "#                                                               #\n"
    #           "#_______________________________________________________________#\n"
    #           "#                 Press 1 to go back to Main Menu               #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 1, message)
    #     if choice == 0:
    #         alt_callback()
    #     else:
    #         callback()

    # def favorites(self, favorites, alt_callback, callback, callback_2, message):
    #     """Function displaying the favorite of the user."""
    #     try:
    #         print("\n\n\n\n\n\n\n\n\n"
    #               "#################################################################\n"
    #               "#####################       FAVORITES       #####################\n"
    #               "###########          Consult your favorite(s)         ###########\n"
    #               "#                                                               #\n")
    #         for i, element in enumerate(favorites):
    #             print(f""" {i + 1}- | {element[0]} | replaced by | {element[1]} | on | {element[2]} |\n""")
    #         print("#_______________________________________________________________#\n"
    #               f"#           !!! Press {i + 3} to delete all the favorites !!!         #\n"
    #               "#         To delete a particular line, press its number         #\n"
    #               f"#                Press {i + 2} to go back to Main Menu                #\n"
    #               "#                       Press 0 to close                        #\n")
    #         choice = int_input(0, i + 3, message)
    #         if choice == 0:
    #             alt_callback()
    #         elif choice in range(1, i + 2):
    #             callback(choice)
    #         elif choice == (i + 3):
    #             callback('all')
    #         else:
    #             callback_2()
    #     except UnboundLocalError:
    #         print("#                                                               #\n"
    #               "#                   No favorite for the moment                  #\n"
    #               "#_______________________________________________________________#\n"
    #               "#                Press 1 to go back to Main Menu                #\n"
    #               "#                       Press 0 to close                        #\n")
    #         choice = int_input(0, 1, message)
    #     if choice == 0:
    #         alt_callback()
    #     else:
    #         callback_2()

    # def favorite_error(self, alt_callback, callback, message):
    #     """Function warning the user that the attempted replacement has already\
    #        been done before."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################       Favorites       #####################\n"
    #           "#                                                               #\n"
    #           "#              !!!THIS REPLACEMENT HAS ALREADY BEEN             #\n"
    #           "#                   ADDED TO YOUR FAVORITES!!!                  #\n"
    #           "#_______________________________________________________________#\n"
    #           "#                 Press 1 to go back to Main Menu               #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 1, message)
    #     if choice == 0:
    #         alt_callback()
    #     else:
    #         callback()

    # def delete_favorites(self, alt_callback, callback, message):
    #     """Function displaying the confirmation message\
    #        that the product is replaced."""
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################       Favorites       #####################\n"
    #           "#                                                               #\n"
    #           "#                   Your favorites are deleted!                 #\n"
    #           "#                                                               #\n"
    #           "#_______________________________________________________________#\n"
    #           "#                 Press 1 to go back to Main Menu               #\n"
    #           "#                       Press 0 to close                        #\n")
    #     choice = int_input(0, 1, message)
    #     if choice == 0:
    #         alt_callback()
    #     else:
    #         callback()
