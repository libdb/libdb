import json
import os


class JSONDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def _save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create(self, key, value):
        if key in self.data:
            raise ValueError(f"Key '{key}' already exists.")
        self.data[key] = value
        self._save_data()

    def bulk_create(self, items):
        for key, value in items.items():
            if key in self.data:
                raise ValueError(f"Key '{key}' already exists.")
            self.data[key] = value
        self._save_data()

    def read(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found.")
        self.data[key] = value
        self._save_data()

    def delete(self, key):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found.")
        del self.data[key]
        self._save_data()

    def list_keys(self):
        return list(self.data.keys())

    def clear(self):
        self.data = {}
        self._save_data()

    def search(self, key, value):
        return {k: v for k, v in self.data.items() if v.get(key) == value}
