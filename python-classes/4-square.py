#!/usr/bin/python3
"""
Class Square that defines a square by size with validation,
and provides getter and setter for size.
"""


class Square:
    """Defines a square with private size, validation, and area method"""

    def __init__(self, size=0):
        self.size = size  

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
