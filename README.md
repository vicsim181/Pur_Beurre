# **How to use Pur Beurre and find healthier food?**

### This application was made with the objective to help consumers finding healthier food than what they usually consume. 

Each user can consult the products from 5 different categories:
-
 * saucisson sec (Dry sausages)
 * jus d'orange (Orange juice)
 * yaourt aux fruits (Fruits yogurt)
 * glace vanille (Vanilla ice cream)

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
