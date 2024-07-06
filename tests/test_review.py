# tests/test_review.py
import unittest
from model.review import Review


class TestReviewModel(unittest.TestCase):

    def test_review_creation(self):
        review = Review(place_id="place1", user_id="user1", rating=5, comment="Great place!")
        self.assertEqual(review.place_id, "place1")
        self.assertEqual(review.rating, 5)


if __name__ == '__main__':
    unittest.main()
