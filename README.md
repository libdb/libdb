# libdb

Easy Management and Creation of Database Based on JSON Format with High Speed and Optimized.

---
- [Installation](#installation)
  - [Install With pip in Windows](#install-with-pip-in-windows)
  - [Install With pip3 in Linux](#install-with-pip3-in-linux)
  - [Install With Git](#install-with-git)
    - [Windows (python)](#windows-python)
    - [Linux (python3)](#linux-python3)
- [Usage](#usage)
  - [Initializing the Database](#initializing-the-database)
  - [Creating a New Entry](#creating-a-new-entry)
  - [Bulk Creating Entries](#bulk-creating-entries)
  - [Updating an Entry](#updating-an-entry)
  - [Deleting an Entry](#deleting-an-entry)
  - [Listing All Keys](#listing-all-keys)
  - [Clearing the Database](#clearing-the-database)
  - [Searching for Entries](#searching-for-entries)
- [Running Tests](#running-tests)
---

## Installation
### Install With `pip` in Windows:
```bash
pip install libdb
```
### Install With `pip3` in Linux:
```bash
# if not installed pip3
sudo apt-get update&&sudo apt-get install python3-pip 
# Install With pip3 command
pip3 install libdb
```
### Install With Git
```bash
git clone https://github.com/libdb/libdb
cd libdb
```
### Git Option's

Windows (python)
```bash
# Install Libdb in windows
python install.py
# Just upgrade libdb in windows
python install.py upgrade
```
Linux (python3)
```bash
# Install Libdb in Linux
python3 install.py
# Just upgrade libdb in Linux
python3 install.py upgrade
```
## Usage

Here are some examples to demonstrate how to use the LibDB package.
### Initializing the Database:
```python
from libdb import JSONDatabase
# Initialize the database
db = JSONDatabase('mydb.json')
```
### Creating a New Entry

```python
db.create('name', 'Alice')
print(db.read('name'))  # Output: Alice
```
### Bulk Creating Entries
```python
items = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}
db.bulk_create(items)
print(db.read('age'))  # Output: 30
print(db.read('city'))  # Output: Wonderland
```
### Updating an Entry
```python
db.update('name', 'Bob')
print(db.read('name'))  # Output: Bob
```

### Deleting an Entry
```python
db.delete('name')
print(db.read('name'))  # Output: None
```
### Listing All Keys
```python
list_keys = db.list_keys()
print(list_keys)  # Output: ['age', 'city']
```
### Clearing the Database
```python
db.clear()
print(db.list_keys())  # Output: []
```
### Searching for Entries
```python
users = {
    'user1': {'name': 'Alice', 'age': 30},
    'user2': {'name': 'Bob', 'age': 25},
    'user3': {'name': 'Charlie', 'age': 30}
}
db.bulk_create(users)
result = db.search('age', 30)
print(result)  # Output: {'user1': {'name': 'Alice', 'age': 30}, 'user3': {'name': 'Charlie', 'age': 30}}
```
## Running Tests
You can run the tests to ensure everything is working correctly:
```bash
python -m unittest discover tests
```
