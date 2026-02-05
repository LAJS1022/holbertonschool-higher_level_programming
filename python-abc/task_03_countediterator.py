#!/usr/bin/env python3
"""Defines a CountedIterator class that keeps track of iteration count."""


class CountedIterator:
    """Custom iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
