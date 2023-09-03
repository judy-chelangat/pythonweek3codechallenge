from sqlalchemy import create_engine
from sqlalchemy import Column,String,ForeignKey,Integer,Sequence

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

# define the database connection 
DATABASE_URI = 'sqlite:///restuarants.db' #path to the database

engine = create_engine(DATABASE_URI,echo=False)
 #creating the engine
Session = sessionmaker(bind=engine) #creating a session
session = Session()
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

    @classmethod
    def fanciest(cls): # returns the restuarant instance for the one with the highest price 
     fancy_restuarant= session.query(cls).order_by(cls.price.desc()).first()
     return fancy_restuarant
    
    #list of all reviews for this restuarant 
    def all_reviews(self):
         list_of_reviews=[]
         for review in self.reviews:
              restuarant_name=self.name
              customer_name=f"{review.customer.first_name} {review.customer.last_name}"
              star_rating= review.star_rating
              one_review= f"Review for {restuarant_name} by {customer_name}: {star_rating} stars."
              list_of_reviews.append(one_review)

         return list_of_reviews
    
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
      
      #customer's favourite restuarant
      def favourite_restuarant(self):
           high_rating=0 
           favorite_restaurant_name = None
           for review in self.reviews: #looping through the reviews 
                if review.star_rating > high_rating:
                     high_rating=review.star_rating
           favorite_restaurant_name = review.restuarant.name
           return favorite_restaurant_name
 
      #add review for a restuarant
      def add_review(self,restuarant_name,rating):
           #creating the new review
           new_review=Review(
                customer=self,
                restuarant=restuarant_name,
                star_rating=rating
           )
           self.reviews.append(new_review)

           session.add(new_review)
           session.commit()

           return new_review


      def delete_reviews(self,restuarant):
           deleted_reviews=[]
           for review in self.reviews:
                if review.restuarant == restuarant:
                     deleted_reviews.append(review)

           for review in deleted_reviews:
                self.reviews.remove(review)
           session.commit()
                
           
      
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
       
       #full review
       def full_review(self):
            return f"Review for {self.restuarant.name} by {self.customer.first_name}:{self.star_rating} stars "
       def __repr__(self):
            return f"Review {self.review_id}: " \
                + f"Customer ID: {self.customer_id}, " \
                + f"Restuarant ID: {self.restuarant_id}, " \
                + f"Rating: {self.star_rating}"