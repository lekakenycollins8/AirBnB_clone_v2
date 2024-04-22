#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {key: value for key, value in FileStorage.__objects.items()
                    if isinstance(value, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if os.path.exists(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) == 0:
            # Handle the case of an empty file
                print("JSON file is empty. No data to load.")
                return
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                try:
                    object_data = json.load(json_file)
                    for key, data in object_data.items():
                        obj_class_name = data.get("__class__")
                        if obj_class_name:
                            if obj_class_name in classes.values():
                                obj_class = classes[obj_class_name]
                                instance = obj_class(**data)
                                FileStorage.__objects[key] = instance
                except FileNotFoundError:
                    pass
                except json.decoder.JSONDecodeError:
                # Handle the case of invalid JSON data
                    print("JSON file contains invalid data. Unable to load.")
                    return
    
    def delete(self, obj=None):
        """deletes obj from __objects if its inside"""
        if obj is None:
            return
        key_to_delete = None
        for key, value in FileStorage.__objects.items():
            if value is obj:
                key_to_delete = key
                break
        if key_to_delete is not None:
            del FileStorage.__objects[key_to_delete]

    def close(self):
        """desrializes JSON file to objects"""
        self.reload()
