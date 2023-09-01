from sqlalchemy import create_engine
from sqlalchemy import Column,String,ForeignKey,Integer,Sequence

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    #relationship
    reviews =relationship('Review',back_populates='restuarant')
    
    #methods to get the restuarant reviews and customers for a restuarant 
    def get_reviews(self):
         return self.reviews
    
    def get_customers(self):
         return [review.customer for review in self.reviews] #returning a specific customer from a review

    def __repr__(self):
        return f"Restuarant {self.restuarant_id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"

#customer table
class Customer(Base):
      __tablename__='customers'
      customer_id=Column(Integer,Sequence('customers_id_seq'),primary_key=True)
      first_name=Column(String)
      last_name=Column(String)

      #relationship
      reviews =relationship('Review',back_populates='customer')

# methods  to retrieve the customer reviews and customers
      def customer_reviews(self):
           return self.reviews
      
      def customer_restuarants(self):
           return [review.restuarant for review in self.reviews]
      
      #customer full name
      def full_name(self):
        return f"{self.first_name} {self.last_name}"

      def __repr__(self):
        return f"Customer {self.customer_id}: " \
            + f"{self.first_name}, " \
            + f"lastname {self.last_name}"

#reviews table 
class Review(Base):
       __tablename__='reviews'
       review_id=Column(Integer,Sequence('review_id_seq'),primary_key=True)
       customer_id =Column(Integer,ForeignKey('customers.customer_id')) # primary key for customer table
       restuarant_id =Column(Integer,ForeignKey('restuarants.restuarant_id'))
       star_rating=Column(Integer)

#establishing the relationships
       customer = relationship('Customer',back_populates='reviews')
       restuarant = relationship('Restuarant', back_populates='reviews')

#class methods for retrieving data
       def get_customer(self):
            return self.customer # returns the customer instance 
       

       def get_restuarant(self):
            return self.restuarant # returns the restuarant instance
       
       
       def __repr__(self):
            return f"Review {self.review_id}: " \
                + f"Customer ID: {self.customer_id}, " \
                + f"Restuarant ID: {self.restuarant_id}, " \
                + f"Rating: {self.star_rating}"