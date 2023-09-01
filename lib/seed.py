from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restuarant,Customer


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restuarants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Restuarant).delete() #to delete the previous recors to avoid duplication
    session.query(Customer).delete()

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
session.bulk_save_objects(restuarants)
session.bulk_save_objects(customers)
session.commit()