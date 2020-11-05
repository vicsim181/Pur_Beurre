"""Script feeding the Category table, using the SQLAlchemy ORM."""
import json
from models.category import Category
from models.base import eng
from sqlalchemy.orm import sessionmaker


def main():
    Session = sessionmaker(bind=eng)
    ses = Session()

    with open('models/settings.json', 'r') as settings:
        data = json.load(settings)

    for category in data['categories']:
        cat = Category(name=category)
        ses.add(cat)
    ses.commit()


if __name__ == "__main__":
    main()
