#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
