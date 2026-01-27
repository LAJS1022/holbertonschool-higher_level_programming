#!/usr/bin/python3
"""
Class Square that defines a square by size with validation.
"""


class Square:
    """Defines a square with private size and validation"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
