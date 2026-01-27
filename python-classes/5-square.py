#!/usr/bin/python3
"""
Class Square that defines a square by size with validation,
area method, and printing capability.
"""


class Square:
    """Defines a square with private size, validation, area, and print method"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("") #
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
