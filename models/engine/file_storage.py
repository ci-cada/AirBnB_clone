#!/usr/bin/python3
"""file_storage.py module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    FileStorage class:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).
        Variables:
        ----------
        new_dict [dict] -- keys and values to build JSON.
        uses JSON dumps to convert the objects to dictionaries.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
    
    @staticmethod
    def json_to_python(json_dict):
        """
        method that takes a dict as an argument and returns an 
        object or the original dict depending on the presence of
        the key "__class__".
        """
        if "__class__" in json_dict:#checks if dict has the key, indicating that there was an object before serialization
            class_name = json_dict["__class__"]#class name obtained from value of key
            if class_name == "BaseModel":#compares class name with basemodel
                return BaseModel(**json_dict)#if matches, new basemodel object created
            else:
                return json_dict#otherwise return original dict
        else:
            return json_dict#if theres no class key return original dict