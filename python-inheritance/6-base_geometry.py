#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
