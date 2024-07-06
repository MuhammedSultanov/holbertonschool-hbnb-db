# tests/test_place.py
import unittest
from model.place import Place


class TestPlaceModel(unittest.TestCase):

    def test_place_creation(self):
        place = Place(name="Test Place", description="A nice place", address="123 Test St",
                      city_id="city1", latitude=12.34, longitude=56.78, host_id="host1",
                      number_of_rooms=3, number_of_bathrooms=2, price_per_night=100,
                      max_guests=4, amenity_ids=["amenity1", "amenity2"])
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.number_of_rooms, 3)
        self.assertEqual(place.price_per_night, 100)

    def test_host_assignment_rule(self):
        place = Place(name="Test Place", description="A nice place", address="123 Test St",
                      city_id="city1", latitude=12.34, longitude=56.78, host_id="host1",
                      number_of_rooms=3, number_of_bathrooms=2, price_per_night=100,
                      max_guests=4, amenity_ids=["amenity1", "amenity2"])
        self.assertEqual(place.host_id, "host1")


if __name__ == '__main__':
    unittest.main()
