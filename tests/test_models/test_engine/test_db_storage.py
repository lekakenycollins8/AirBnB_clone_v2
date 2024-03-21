#!/usr/bin/python3
"""test database storage"""

import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.db_storage import DBStorage
from sqlalchemy.orm.session import Session
import os

class TestDBStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        # Set up environment variables for testing database
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'

        # Initialize DBStorage instance
        cls.storage = DBStorage()

        # Create tables and database session
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down test class"""
        # Close database session
        Session.close_all()
        # Drop all tables
        cls.storage.__session.close()
        cls.storage.__engine.dispose()

    def setUp(self):
        """Set up individual test"""
        # Start a new session for each test
        self.session = self.storage._DBStorage__session()

    def tearDown(self):
        """Tear down individual test"""
        # Rollback any changes made during the test
        self.session.rollback()
        # Close the session
        self.session.close()

    def test_all_method(self):
        """Test the all method"""
        # Add objects to the session
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        self.session.add(state)
        self.session.add(city)
        self.session.commit()

        # Retrieve all objects from the session
        objects = self.storage.all()

        # Check if objects were retrieved
        self.assertTrue(len(objects) > 0)

    def test_new_method(self):
        """Test the new method"""
        # Create a new object
        state = State(name="California")
        # Add the object to the session
        self.storage.new(state)
        # Check if the object is in the session
        self.assertIn(state, self.session)

    def test_save_method(self):
        """Test the save method"""
        # Create a new object
        state = State(name="California")
        # Add the object to the session
        self.storage.new(state)
        # Save changes to the session
        self.storage.save()
        # Check if changes were saved
        self.assertTrue(state.id is not None)

    def test_delete_method(self):
        """Test the delete method"""
        # Create a new object
        state = State(name="California")
        # Add the object to the session
        self.storage.new(state)
        # Delete the object from the session
        self.storage.delete(state)
        # Check if the object is no longer in the session
        self.assertNotIn(state, self.session)

    def test_reload_method(self):
        """Test the reload method"""
        # Save current session
        prev_session = self.storage._DBStorage__session()
        # Reload the session
        self.storage.reload()
        # Check if the session has changed
        self.assertNotEqual(prev_session, self.storage._DBStorage__session())

if __name__ == '__main__':
    unittest.main()

