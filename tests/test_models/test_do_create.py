import unittest
from unittest.mock import patch
from datetime import datetime
import os
import uuid

# Assuming HBNBCommand and other necessary dependencies are imported

class TestCreateMethod(unittest.TestCase):
    @patch('builtins.print')
    def test_create_missing_class_name(self, mocked_print):
        cmd = HBNBCommand()
        cmd.do_create("")
        mocked_print.assert_called_with("** class name missing **")

    @patch('builtins.print')
    def test_create_nonexistent_class(self, mocked_print):
        cmd = HBNBCommand()
        cmd.do_create("NonExistentClass")
        mocked_print.assert_called_with("** class doesn't exist **")

    @patch('builtins.print')
    def test_create_missing_attributes(self, mocked_print):
        cmd = HBNBCommand()
        cmd.do_create("ExistingClass")
        mocked_print.assert_called_with("** attributes missing **")

    @patch('builtins.print')
    def test_create_with_valid_input(self, mocked_print):
        cmd = HBNBCommand()
        with patch.object(os, 'getenv', return_value='db'):
            with patch.object(uuid, 'uuid4', return_value='mocked_uuid'):
                with patch.object(datetime, 'now', return_value='mocked_datetime'):
                    cmd.do_create("ExistingClass attr1=5 attr2='value'")
        mocked_print.assert_called_with('mocked_uuid')

if __name__ == '__main__':
    unittest.main()
