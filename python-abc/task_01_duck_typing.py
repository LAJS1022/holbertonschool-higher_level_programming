#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math
"""Create a class"""


class Shape(ABC):
    """Create Abstract class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Create Circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Create Rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """print area and perimeter"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter:{shape.perimeter()}")
