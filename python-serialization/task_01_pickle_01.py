#!/usr/bin/env python3
"""Defines a CustomObject class with pickle serialization and deserialization."""

import pickle


class CustomObject:
    """Custom class with attributes and serialization methods."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The file to load the serialized object from.

        Returns:
            CustomObject or None: The deserialized object, or None if error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
