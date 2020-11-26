

def int_input(min_nb, max_nb, message):
    while True:
        raw = input(message)
        if raw.isdigit():
            nb = int(raw)
            if nb in range(min_nb, max_nb + 1):
                return nb
        print(f'Please enter an integer between \
{min_nb} and {max_nb} included.')

def manage_cat(choice):
    print(choice)




class Menu:
    def __init__(self, title, subtitle, choices, information=''):
        self.title = title
        self.subtitle = subtitle
        self.choices = choices
        self.information = information

    def run(self):
        self.print()
        self.input()
    
    # def print_header(self):
    #     print("\n\n\n\n\n\n\n\n\n"
    #           "#################################################################\n"
    #           "#####################{:^22}".format(self.name), "#####################\n"
    #           "###########{:^42}".format(self.action), "###########\n"
    #           "#                                                               #")

    # def print_middle(self, *args):
    #     for i, arg in enumerate(args):
    #         argument = str(i + 1) + "- " + arg
    #         print("#                   {:<43}".format(argument), "#")
    #     print("#                                                               #\n"
    #           "#_______________________________________________________________#")

    # def print_bottom(self, *args):
    #     for arg in args:
    #         print("#{:^62}".format(arg), "#")

    # def print_product(self):
    #     print("#{:^62}".format(self.subtitle), "#\n")
    #     print(f" -Name: {self.product.name}\n"
    #           f" -Quantity: {self.product.quantity}\n"
    #           f" -Nutriscore: {self.product.nutri_score}\n"
    #           f" -Ingredients: {self.product.ingredients}\n"
    #           f" -URL: {self.product.link_url}\n"
    #           f" -Store(s): {self.product.stores}\n")
    #     print("#                                                               #\n"
    #           "#_______________________________________________________________#")

    # def print_all(self):
    #     self.print_header()
    #     self.print_middle()
    #     if self.product:
    #         self.print_product()
    #     self.print_bottom()

    def print(self):
        print(self.title)
        print(self.subtitle)
        print(self.information)
        for i, choice in enumerate(self.choices):
            if 'special' in choice and choice['special']:
                name = choice['name']
                print(f' {i}- {name}')
        for i, choice in enumerate(self.choices):
            if 'special' in choice and not choice['special']:
                name = choice['name']
                print(f' {i}- {name}')

    def input(self):
        choice_user = int_input(0, len(self.choices), 'Press your choice: ')
        choice = self.choices[choice_user]
        choice['callback'](choice['payload'])


class CategoryMenu(Menu):
    def __init__(self, categories, on_leaving, on_category_choice):
        choices = []
        choices.append({'special': True, 'name': 'leaving', 'callback': on_leaving})
        # choices.append({'special': True, 'name': 'return main menu', 'callback': on_leaving})
        for category in categories:
            choices.append({'special': False, 'name': category, 'callback': on_category_choice, 'payload': {'cat_name': category}})
        # choices.append('special')
        super().__init__('CATEGORIES', 'Select a category', choices)

# menu = Menu("Main Menu", "Select an action", [{'name': 'Pain chocolat', 'callback': manage_cat, 'payload': {'cat_name': 'Pain chocolat'}},
#                                               {'name': 'Coca', 'callback': manage_cat, 'payload': {'cat_name': 'Coca'}}])
# menu.print()
# menu.input()

categroy = CategoryMenu(['Pain Chocolat', 'Coca'], exit, manage_cat)
categroy.run()


