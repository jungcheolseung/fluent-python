"""
220511
챕터 1
"""

from math import hypot
# https://docs.python.org/ko/3/library/math.html?highlight=hypot#math.hypot


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.x, self.y)
        # https://docs.python.org/ko/3/library/functions.html#repr
        # https://docs.python.org/ko/3/library/string.html?highlight=r%20string#format-examples
        # https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
        # return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)
print(abs(v * 3))
