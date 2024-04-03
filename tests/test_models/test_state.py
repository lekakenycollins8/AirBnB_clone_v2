#!/usr/bin/python3
""" """
import unittest
import MySQLdb
from models.state import State
from models.base_model import BaseModel
from models import storage

class TestState(unittest.TestCase):
    def setUp(self):
        # Establish connection to the MySQL database
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_state(self):
        # Get the initial count of records in the states table
        initial_count = len(storage.all(State))

        # Execute the console command
        new_state = State(name="California")
        new_state.save()

        # Get the count of records in the states table after adding a new state
        final_count = len(storage.all(State))

        # Assert if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()
