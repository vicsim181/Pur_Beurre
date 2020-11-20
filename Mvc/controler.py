"""File holding the Controler Class, managing the actions coming from the client."""
from Mvc.views import Main, Category, Product, Favorite
from Mvc.model import Model
from Mvc.utils import leaving


class Controler():
    """Class holding the controler and its functions."""

    def display_main_menu():
        """Function displaying the Main Menu in the console line."""
        Main.display_view(leaving, Controler.display_categories, Controler.display_favorites, "What's your choice? : ",
                          "MAIN MENU", "Select an action to perform")

    def display_categories():
        """Function displaying the categories selection menu."""
        categories = Model.get_categories()
        Category.display_categories(categories, leaving, Controler.display_products, Controler.display_main_menu,
                                    "Please select a Category by entering its number: ", "REPLACING A PRODUCT",
                                    "Select a category of products")

    def display_products(category_id, i):
        """Function displaying the products from the selected category."""
        product, category_name, stores, max_cat = Model.get_products(category_id, i)
        Product.display_products(category_name.title(), category_id, product, i, str(stores), leaving,
                                 Controler.save_product, Controler.display_products, Controler.display_main_menu, None,
                                 "Please select an action: ", max_cat, "REPLACING A PRODUCT",
                                 "Select the product to replace")

    def save_product(product, category_id, category_name):
        """Function saving the product for a later use."""
        replaced_product = product
        Controler.replacement_suggestion(product.Id, product.id_category, replaced_product, category_name)

    def replacement_suggestion(product_id, id_category, replaced_product, category_name):
        """Function displaying the selection of suggestions to replace the product previously selected."""
        suggestion, stores = Model.generate_suggestions(product_id, id_category)
        Product.display_suggestions(suggestion, 0, stores, leaving, Controler.display_replacement,
                                    Product.display_suggestions, Controler.display_main_menu, replaced_product,
                                    "Please select an action: ", 5, "REPLACING A PRODUCT",
                                    "Select the alternative product")

    def display_replacement(suggestion, replaced_product):
        """Function displaying the confirmation of replacement."""
        test = Model.replace(replaced_product, suggestion.Id)
        if test == 'ok':
            Favorite.save_successful(leaving, Controler.display_main_menu, "REPLACEMENT SAVED", '',
                                     "Your product has been replaced successfully",
                                     "You can consult it in your favorites", "Please select an action: ")
        elif test == 'nok':
            Favorite.save_unsuccessful(leaving, Controler.display_main_menu, "REPLACEMENT FAILED", '',
                                       "Your replacement has already been saved",
                                       "You can consult it in your favorites", "Please select an action: ")

    def display_favorites():
        """Function displaying the favorites menu."""
        favorites = Model.get_favorites()
        Favorite.consult(favorites, leaving, Controler.display_delete_favorites, Controler.display_main_menu,
                         "FAVORITES", "Consult your favorite(s)", "Please select an action: ")

    def display_delete_favorites(choice):
        """Function displaying the confirmation of delete."""
        if choice == 'all':
            Model.delete_all_favorites()
            Favorite.display_delete_all("FAVORITES", "Your favorites have been deleted", "No favorite",
                                        "Press 1 to go back to Main Menu", "Press 0 to close",
                                        "Please select an action: ", leaving, Controler.display_main_menu)
        else:
            Model.delete_favorites(choice)
        Controler.display_favorites()
