# libdb

A simple JSON database manager for Python.

## Installation

```bash
pip install libdb
```

## Usage

```python
from libdb import JSONDatabase

# Initialize the database
db = JSONDatabase('mydb.json')

# Create a new entry
db.create('name', 'Alice')

# Read an entry
print(db.read('name'))  # Output: Alice

# Update an entry
db.update('name', 'Bob')

# Delete an entry
db.delete('name')

# List all keys
print(db.list_keys())  # Output: []

# Clear the database
db.clear()

# Bulk create entries
items = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}
db.bulk_create(items)

# Search for entries
users = {
    'user1': {'name': 'Alice', 'age': 30},
    'user2': {'name': 'Bob', 'age': 25},
    'user3': {'name': 'Charlie', 'age': 30}
}
db.bulk_create(users)
result = db.search('age', 30)
print(result)  # Output: {'user1': {'name': 'Alice', 'age': 30}, 'user3': {'name': 'Charlie', 'age': 30}}

```