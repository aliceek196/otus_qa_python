from otus_qa_python.src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("You can't create a circle")
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * self.radius * self.radius
