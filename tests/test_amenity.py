# tests/test_amenity.py
import unittest
from model.amenity import Amenities


class TestAmenitiesModel(unittest.TestCase):

    def test_amenities_creation(self):
        amenity = Amenities(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")


if __name__ == '__main__':
    unittest.main()
