from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restuarant,Customer,Review


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restuarants.db') #establishing the connection
    Session = sessionmaker(bind=engine) #creating a session
    session = Session()
    session.query(Restuarant).delete() #to delete the previous records to avoid duplication
    session.query(Customer).delete()
    session.query(Review).delete()

#to check if its working 
#print("Seeding restuarants...")
#data for the restuarants
restaurant_names = [
    "Nairobi Grill House",
    "Safari Bites",
    "Savannah Spice",
    "Simba Steakhouse",
    "Maasai Kitchen",
    "Kilimanjaro Delights",
    "Jambo Cafe",
    "African Fusion",
    "Nairobi Noodle House",
    "Savanna Sizzle",
]
restuarants = [
    Restuarant(
        name=random.choice(restaurant_names),
        price=random.randint(0, 60)
    )
for i in range(10)] #creating 10 records 

#adding records for the customers 
#print("seeding customers")
customers =[
    Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    for j in range(10)
]

#saving the restuarants,customers  to the database 
session.add_all(restuarants)
session.add_all(customers)
session.commit()

#adding records for the reviews
#print('seeding reviews')
reviews = [
        Review(
              customer=random.choice(customers),  # Using  the actual Customer object
              restuarant=random.choice(restuarants), #random choice from the restuarant
              star_rating=random.randint(1, 5)
        )
        for k in range(10)  # Generating 10 reviews
    ]


#adding reviews to the session and commiting 
session.add_all(reviews)
session.commit()

#querying the data to get results
#1 getting the customer,restuarant  instance from a review
review1 = session.query(Review).first()

customer_instance = review1.get_customer()
restaurant_instance = review1.get_restuarant()

print("------------------customer and restuarant instance-----------------------")
print (customer_instance)
print(restaurant_instance)

#2 getting the reviews for  a restuarant 
restaurant1 = session.query(Restuarant).first()  # Retrieving  a restaurant

restaurant_reviews= restaurant1.get_reviews()   #using the method to get the reviews for a restuarant
restuarant_customers = restaurant1.get_customers() #getting the customers who have reviewed a particular restuarant

print("------------------reviews and customers of a particular restuarant-----------------------")
print(restaurant_reviews)
print(restuarant_customers)

#3 getting the customer reviews and customer restuarants (the ones one has reviewed)
customer1 = session.query(Customer).first()  # Retrieve a customer

reviews_collection = customer1.customer_reviews()
restaurants_collection = customer1.customer_restuarants()

print("------------------customer and restuarant reviews -----------------------")
print(restaurants_collection)
print(reviews_collection)

#4 printing the customer full name 
customer = session.query(Customer).first()  # Retrieve a customer
full_name = customer.full_name()

print("------------------customer's full name---------------- ")
print(full_name)

#5 getting the customers favourite restuarant
print("-------------------customer's favourite restuarant-------------")
print(customer1.favourite_restuarant())

# # 6 adding a review of a restuarant
# customer2 = session.query(Customer) 
# restaurant2 = session.query(Restuarant)  
# rating=5 #setting the rating 
# new_review=Customer.add_review(restaurant2,rating)

# print("---------------------added review---------------")
# print(new_review)

#7 deleting reviews
#8 full review 
review2 = session.query(Review).first()  # Replace with the desired review
full_review = review2.full_review()

print("------------------full review-----------")
print(full_review)
#closing the session
session.close()