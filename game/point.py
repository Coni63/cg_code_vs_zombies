from __future__ import annotations

import math


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, p: Point) -> float:
        return math.sqrt(self.distance2(p))

    def distance2(self, p: Point) -> float:
        dx = p.x - self.x
        dy = p.y - self.y
        return dx * dx + dy * dy

    def describe(self):
        print(self.__repr__())

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def getNorm(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def setNorm(self, norm: float):
        length = self.getNorm()
        self.x *= norm / length
        self.y *= norm / length

    def clone(self):
        return Point(self.x, self.y)

    def round(self):
        self.x = math.trunc(self.x)
        self.y = math.trunc(self.y)

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int | float):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int | float):
        if scalar == 0:
            raise ZeroDivisionError
        return Point(self.x / scalar, self.y / scalar)

    def __rmul__(self, scalar: int | float):
        return Point(scalar * self.x, scalar * self.y)

    def __rtruediv__(self, scalar: int | float):
        if scalar == 0:
            raise ZeroDivisionError
        return Point(self.x / scalar, self.y / scalar)

    def __eq__(self, other: Point):
        if other is None:
            return False

        if self is other:
            return True

        if self.__class__ != other.__class__:
            return False

        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other
