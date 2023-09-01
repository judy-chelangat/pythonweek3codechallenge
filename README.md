# Restaurant Review Management System

## Overview

This README file outlines the deliverables for the Restaurant Review Management System project. The project involves managing reviews for restaurants, customers, and their relationships using SQLAlchemy. Three main classes are involved: `Restaurant`, `Customer`, and `Review`, each with specific methods and relationships.

## Getting Started

Before you begin working on the project deliverables, make sure you have set up your environment and created the necessary tables using SQLAlchemy. Ensure that you have executed the migration to create the required database tables.

### Prerequisites

- Python (3.7+)
- SQLAlchemy
- SQLite (or any other database of your choice)

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip`:
3. Run the migration to create the database tables:
4. Use the `seeds.py` file to populate the database with initial data for testing:


Now that you have set up the project, you can proceed with implementing the deliverables.

## Migrations

Before working on other deliverables, you need to create a migration for all tables. The `reviews` table should have the following columns:

- `id` (primary key)
- `restaurant_id` (foreign key to `Restaurant`)
- `customer_id` (foreign key to `Customer`)
- `star_rating` (integer)

Ensure that the relationships between `Review`, `Restaurant`, and `Customer` are properly established in the migration.

## Object Relationship Methods

### Review

- `Review.customer()`: Returns the `Customer` instance for this review.
- `Review.restaurant()`: Returns the `Restaurant` instance for this review.

### Restaurant

- `Restaurant.reviews()`: Returns a collection of all the reviews for the `Restaurant`.
- `Restaurant.customers()`: Returns a collection of all the customers who reviewed the `Restaurant`.

### Customer

- `Customer.reviews()`: Returns a collection of all the reviews that the `Customer` has left.
- `Customer.restaurants()`: Returns a collection of all the restaurants that the `Customer` has reviewed.

Ensure that these methods work as expected by querying the database using SQLAlchemy. For example, `session.query(Customer).first().restaurants` should return a list of restaurants for the first customer in the database based on the seed data.

## Aggregate and Relationship Methods

### Customer

- `Customer.full_name()`: Returns the full name of the customer, with the first name and the last name concatenated in Western style.
- `Customer.favorite_restaurant()`: Returns the restaurant instance that has the highest star rating from this customer.
- `Customer.add_review(restaurant, rating)`: Creates a new review for the restaurant with the given `restaurant_id` and rating.
- `Customer.delete_reviews(restaurant)`: Removes all reviews by the customer for a specific restaurant.

### Review

- `Review full_review()`: Returns a string formatted as follows: Review for {restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

### Restaurant

- `Restaurant fanciest(), this method should be a class method`: Returns one restaurant instance for the restaurant that has the highest price.
- `Restaurant all_reviews()`: Returns a list of strings with all the reviews for this restaurant 


## License

This project is licensed under the [MIT License](LICENSE).

## Author

Author: Judy chelangat




