from math import pi


class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2
