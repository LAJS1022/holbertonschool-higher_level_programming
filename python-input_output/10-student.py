#!/usr/bin/python3
"""Defines a Student class with JSON serialization and filtering."""


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
