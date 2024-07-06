# tests/test_base_model.py
import unittest
from model.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_creation(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_base_model_save_method(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
