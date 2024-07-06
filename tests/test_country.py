# tests/test_country.py
import unittest
from model.country import Country


class TestCountryModel(unittest.TestCase):

    def test_country_creation(self):
        country = Country(name="Turkey", code="TR")
        self.assertEqual(country.name, "Turkey")
        self.assertEqual(country.code, "TR")


if __name__ == '__main__':
    unittest.main()
