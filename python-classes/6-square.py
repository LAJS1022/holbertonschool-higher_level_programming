#!/usr/bin/python3
"""
This module defines the Square class.
The Square represents a geometric square defined by its size and position.
It validates that size is a non-negative integer and position is a tuple
of two non-negative integers. It can compute its area and print itself
using the character '#', respecting its position offsets.
"""


class Square:
    """
    This class defines a square by its size and position.
    The size attribute is private to ensure type and value control.
    The position attribute is private to ensure proper formatting
    when printing the square. Getter and setter methods are provided
    to safely retrieve and update these attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position offset (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position offset of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 non-negative integers.

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.

        The square is printed respecting its position offsets:
        - position[0] adds spaces before each line.
        - position[1] adds newlines before the square.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
