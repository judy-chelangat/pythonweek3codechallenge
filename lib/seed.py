from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restuarant,Customer,Review


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restuarants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Restuarant).delete() #to delete the previous records to avoid duplication
    session.query(Customer).delete()
    session.query(Review).delete()

#to check if its working 
print("Seeding restuarants...")
restuarants = [
    Restuarant(
        name=fake.name(),
        price=random.randint(0, 60)
    )
for i in range(10)] #creating 10 records 

#adding records for the customers 
print("seeding customers")
customers =[
    Customer(
        first_name=fake.name(),
        last_name=fake.name()
    )
    for j in range(10)
]

#saving the restuarants,customers  to the database 
session.add_all(restuarants)
session.add_all(customers)
session.commit()

#adding records for the reviews
print('seeding reviews')
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

#closing the session
session.close()