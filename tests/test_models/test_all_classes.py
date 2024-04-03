#!/usr/bin/python3
"""tests for all hbnb classes"""

import unittest
import MySQLdb
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage

class TestCity(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_city(self):
        # Get the initial count of records in the cities table
        initial_count = len(storage.all(City))

        # Execute the console command
        new_city = City(name="San Francisco", state_id="CA")
        new_city.save()

        # Get the count of records in the cities table after adding a new city
        final_count = len(storage.all(City))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

# Similar tests can be written for other modules: Place, User, Amenity, Review

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_place(self):
        # Get the initial count of records in the places table
        initial_count = len(storage.all(Place))

        # Execute the console command
        new_place = Place(name="Cozy Apartment", city_id="1", user_id="1")
        new_place.save()

        # Get the count of records in the places table after adding a new place
        final_count = len(storage.all(Place))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

class TestUser(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_user(self):
        # Get the initial count of records in the users table
        initial_count = len(storage.all(User))

        # Execute the console command
        new_user = User(email="test@example.com", password="password")
        new_user.save()

        # Get the count of records in the users table after adding a new user
        final_count = len(storage.all(User))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

class TestAmenity(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_amenity(self):
        # Get the initial count of records in the amenities table
        initial_count = len(storage.all(Amenity))

        # Execute the console command
        new_amenity = Amenity(name="Wifi")
        new_amenity.save()

        # Get the count of records in the amenities table after adding a new amenity
        final_count = len(storage.all(Amenity))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

class TestReview(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_review(self):
        # Get the initial count of records in the reviews table
        initial_count = len(storage.all(Review))

        # Execute the console command
        new_review = Review(text="Great experience!", place_id="1", user_id="1")
        new_review.save()

        # Get the count of records in the reviews table after adding a new review
        final_count = len(storage.all(Review))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()

