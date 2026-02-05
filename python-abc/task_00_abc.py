#!/usr/bin/python3
"""Defines an abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound of a Dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound of a Cat."""
        return "Meow"
