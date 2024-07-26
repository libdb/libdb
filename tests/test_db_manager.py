import unittest
import os
from libdb.db_manager import JSONDatabase


class TestJSONDatabase(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_db.json'
        self.db = JSONDatabase(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_read(self):
        self.db.create('name', 'Alice')
        self.assertEqual(self.db.read('name'), 'Alice')

    def test_bulk_create(self):
        items = {
            'name': 'Alice',
            'age': 30,
            'city': 'Wonderland'
        }
        self.db.bulk_create(items)
        self.assertEqual(self.db.read('name'), 'Alice')
        self.assertEqual(self.db.read('age'), 30)
        self.assertEqual(self.db.read('city'), 'Wonderland')

    def test_update(self):
        self.db.create('name', 'Alice')
        self.db.update('name', 'Bob')
        self.assertEqual(self.db.read('name'), 'Bob')

    def test_delete(self):
        self.db.create('name', 'Alice')
        self.db.delete('name')
        self.assertIsNone(self.db.read('name'))

    def test_list_keys(self):
        self.db.create('name', 'Alice')
        self.db.create('age', 30)
        self.assertListEqual(self.db.list_keys(), ['name', 'age'])

    def test_clear(self):
        self.db.create('name', 'Alice')
        self.db.clear()
        self.assertEqual(self.db.list_keys(), [])

    def test_search(self):
        items = {
            'user1': {'name': 'Alice', 'age': 30},
            'user2': {'name': 'Bob', 'age': 25},
            'user3': {'name': 'Charlie', 'age': 30}
        }
        self.db.bulk_create(items)
        result = self.db.search('age', 30)
        expected = {
            'user1': {'name': 'Alice', 'age': 30},
            'user3': {'name': 'Charlie', 'age': 30}
        }
        self.assertDictEqual(result, expected)

    def test_create_existing_key(self):
        self.db.create('name', 'Alice')
        with self.assertRaises(ValueError):
            self.db.create('name', 'Bob')

    def test_bulk_create_existing_key(self):
        self.db.create('name', 'Alice')
        items = {
            'name': 'Bob',
            'age': 30
        }
        with self.assertRaises(ValueError):
            self.db.bulk_create(items)

    def test_update_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.db.update('name', 'Bob')

    def test_delete_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.db.delete('name')


if __name__ == '__main__':
    unittest.main()
