#!/usr/bin/env python3
"""Defines a VerboseList class that extends Python's built-in list."""


class VerboseList(list):
    """Custom list that prints notifications when modified."""

    def append(self, item):
        """Append item and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and notify."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and notify."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and notify."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
