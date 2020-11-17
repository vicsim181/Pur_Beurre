# **How to use Pur Beurre and find healthier food?**

### This application was made with the objective to help consumers finding healthier food than what they usually consume. 

Each user can consult the products from 5 different categories:
-
 * Apéritif (Apetizer)
 * Biscuit chocolat (Chocolate biscuits)
 * jus d'orange (Orange juice)
 * yaourt aux fruits (Fruits yogurt)
 * glace chocolat (Chocolate ice cream)

Those products are based on what is available in the french market and stores, the data about thoses products are extracted from the OpenFoodFacts database. 


## How to install the application?

First of all you need to install Python 3.8 or later version.

Following this you need to clone repo and install all the dependencies:

```bash
> git clone https://github.com/vicsim181/Pur_Beurre.git
> cd Pur_Beurre
> pip install -r requirements.txt
```

Once they are installed, we need to create the database, in this documentation we use MySQL.
You can find the documentation related to MySQL [here](https://dev.mysql.com/doc/).

In the Pur_Beurre folder you can find different files and folders, one of those is named Scripts. 
It's inside this folder that the scripts creating and feeding the database are located. 
These scripts use the ORM of SQLAlchemy, they also import elements from other files located in the Models folder.
In the Models file, open 'base.py'. You can see those two lines:
```python
password = os.environ['MySQL_password']

eng = create_engine(f'mysql://root:{password}@localhost/database?charset=utf8mb4')
``` 
The password has been as an Environment variable. It is recommended to do so in order to keep the password secret, you can set the variable's name as you wish.
Remember to use the correct password for the user profile you chose to use (here 'root').
Remember also to modify the name of the database and replace it by the name of the one you created previously. 
Once this modification is done, you can create and feed the tables as follow:
```bash
> py ormcreatedb.py
> py ormcreatecategories.py
> py ormfeed.py
```

Your database should now host 5 tables:
* category
* favorite
* product
* store
* store_product


## How to use the application?

Once the application is ready to use, launch it with the following file:
```python
> py purbeurre.py
```

The main menu of the application will then be visible.

![Main Menu](/Pictures/mainmenu.jpg)

Two options are implemented, the first one allows you to choose a category in order to consult the available products:

![Categories](/Pictures/categories.jpg)

You can then iterate through the products of the chosen category:

![Products](/Pictures/products1.jpg)

![Products](/Pictures/products2.jpg)

![Products](/Pictures/products3.jpg)

![Products](/Pictures/products4.jpg)

When you found one you would like to replace by another, just select it by pressing 1.

![Alternative](/Pictures/alternative.jpg)

The application will propose you the 5 best products of the same category (apart from the previous selected one). 
If a product matches your wish cou can choose it by pressing 1 again. It will be saved into the favorites table, which you can consult at any moment from the main menu.
In order to do so, just press 2 when on the main menu:

![Favorites](/Pictures/favorites.jpg)

The favorites view shows you what products have been replaced by others and at what date and time.
You can delete all the table or a specific line by pressing the adequate command.

![Deletion](/Pictures/deletion.jpg)

## Technical details

The tables have been implemented with foreign keys and relationships. Deleting data from a table might affect other tables as well.

For example, the Store and the StoreProduct tables are linked, if a store was to be removed from the Store table, it wouldn't be possible to find the products it sells anymore. 

Therefore, the StoreProduct table would also see the lines with the store being removed. The same with a deleted product also works.

Finally the Favorite table is linked the same way, if a product was to be deleted from the Product table, the lines in the Favorite table including this product will be deleted as well.


