from sqlalchemy import create_engine
from sqlalchemy import Column,String,ForeignKey,Integer,Sequence

from sqlalchemy.ext.declarative import declarative_base

# define the database connection 
DATABASE_URI = 'sqlite:///restuarants.db' #path to the database

engine = create_engine(DATABASE_URI,echo=True)
 #creating the engine

#base class for allthe classes
Base =declarative_base()

#restuarant table
class Restuarant(Base):
    __tablename__='restuarants'
    restuarant_id=Column(Integer ,Sequence('resturant_id_seq'), primary_key=True)
    name =Column(String)
    price =Column(Integer)


def __repr__(self):
        return f"Restuarant {self.restuarant_id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"

#customer table
class Customer(Base):
      __tablename__='customers'
      customer_id=Column(Integer,Sequence('customer_id_seq'),primary_key=True)
      first_name=Column(String)
      last_name=Column(String)


def __repr__(self):
        return f"Customer {self.customer_id}: " \
            + f"{self.first_name}, " \
            + f"lastname {self.last_name}"