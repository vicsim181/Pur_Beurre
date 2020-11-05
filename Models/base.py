"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

password = os.environ['MySQL_password']

eng = create_engine(f'mysql://root:{password}@localhost/essai', echo=True)

Base = declarative_base()
