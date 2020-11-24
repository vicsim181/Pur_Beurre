"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

password = os.environ['MySQL_password']

eng = create_engine(f'mysql://root:{password}@localhost/purbeurre?charset=utf8mb4')

Base = declarative_base()
