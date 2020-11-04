"""Script feeding the Category table, using the SQLAlchemy ORM."""
import json
from ormcreation import Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

eng = create_engine('mysql://opcr5:japon+72@#cclmvdf@localhost/essai', echo=True)
Session = sessionmaker(bind=eng)
ses = Session()

with open('./Scripts/settings.json', 'r') as settings:
    data = json.load(settings)

for category in data['categories']:
    cat = Category(name=category)
    ses.add(cat)
ses.commit()    