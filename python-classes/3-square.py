#!/usr/bin/python3
"""
Class Square that defines a square by size with validation and area method.
"""


class Square:
    """Defines a square with private size, validation, and area method"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
