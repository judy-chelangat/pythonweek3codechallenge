from sqlalchemy import create_engine
from sqlalchemy import Column,String,ForeignKey,Integer

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restuarants.db')

Base =declarative_base