"""Script feeding the Category table, using the SQLAlchemy ORM."""
import json
import sys
sys.path.append('D:/Github/P5/github')
from Models.category import Category
from Models.base import eng
from sqlalchemy.orm import sessionmaker


def main():
    Session = sessionmaker(bind=eng)
    ses = Session()

    with open('../models/settings.json', 'r') as settings:
        data = json.load(settings)

    for category in data['categories']:
        cat = Category(name=category)
        ses.add(cat)
    ses.commit()


if __name__ == "__main__":
    main()
