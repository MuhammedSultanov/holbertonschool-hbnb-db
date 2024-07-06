from persistence.ipersistence_manager import IPersistenceManager
from collections import defaultdict
import json
import os


class DataManager(IPersistenceManager):
    def __init__(self, storage_file="data.json"):
        self.storage_file = storage_file
        if not os.path.exists(storage_file):
            with open(storage_file, "w") as f:
                f.write("{}")

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id')  #, None
        with open('data.json', 'r') as data:
            dataStore = json.load(data)
        if entity_type not in dataStore:
            dataStore[entity_type] = {}
        #key = f"{entity_type}_{entity_id}"
        dataStore[entity_type][entity_id] = entity.__dict__
        with open('data.json', 'w') as da:
            json.dump(dataStore, da, indent=2)
        return dataStore[entity_type][entity_id]

    def get(self, entity_id, entity_type):
        with open('data.json', 'r') as data:
            dataStore = json.load(data)
        if entity_type in dataStore and str(entity_id) in dataStore[entity_type]:
            return dataStore[entity_type][entity_id]
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")
        
    def update(self, entity):
        with open('data.json', 'r') as data:
            dataStore = json.load(data)
        entity_id = getattr(entity, "id")
        entity_type = type(entity).__name__
        if entity_type in dataStore :
            dataStore[entity_type][entity_id] = entity.__dict__
            with open('data.json', 'w') as da:
                json.dump(dataStore, da, indent=2)
            print(f"Entity {entity_type} with id {entity_id} updated.")
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")


    def delete(self, entity_id, entity_type):
        with open('data.json', 'r') as data:
            dataStore = json.load(data)
        if entity_type in dataStore and str(
                entity_id) in dataStore[entity_type]:
            del dataStore[entity_type][entity_id]
            with open('data.json', 'w') as da:
                json.dump(dataStore, da, indent=2)
        else:
            print(f"Entity {entity_type} with id {entity_id} not found.")

