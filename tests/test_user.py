# tests/test_user.py

import unittest
from model.base_model import BaseModel
from model.user import User


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        email = 'test@example.com'
        first_name = 'John'
        last_name = 'Doe'
        user = User(email, first_name, last_name)

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

    def test_default_values(self):
        email = 'test@example.com'
        user = User(email)

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_inheritance(self):
        email = 'test@example.com'
        user = User(email)

        self.assertIsInstance(user, BaseModel)


if __name__ == '__main__':
    unittest.main()

