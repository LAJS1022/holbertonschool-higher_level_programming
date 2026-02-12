#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
