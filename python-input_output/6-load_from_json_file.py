#!/usr/bin/python3
"""Defines a function to create an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The deserialized Python object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
