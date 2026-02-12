#!/usr/bin/python3
"""Defines a function to read a text file and print its contents."""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
