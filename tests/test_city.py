# tests/test_city.py
import unittest
from model.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City(name="Test City", country_code="123")

    def test_city_initialization(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertEqual(self.city.country_code, "123")


if __name__ == "__main__":
    unittest.main()
