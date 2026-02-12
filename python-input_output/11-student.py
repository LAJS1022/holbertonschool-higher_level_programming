#!/usr/bin/python3
"""Defines a Student class with JSON serialization, filtering, and reloading."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
            If None, all attributes are returned.

        Returns:
            dict: Dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values
        from the given dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
