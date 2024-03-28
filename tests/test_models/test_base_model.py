import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected = '[BaseModel] ({}) {}'.format(
            self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(
            model_dict['created_at'], self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'], self.model.updated_at.isoformat()
        )
        self.assertNotIn('_sa_instance_state', model_dict)

    def test_delete(self):
        self.model.delete()
        # Here you should test if the model is deleted from storage


if __name__ == '__main__':
    unittest.main()
