from otus_qa_python.src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_x, side_y, side_z):
        super().__init__(name="Triangle")
        if any(side <= 0 for side in (side_x, side_y, side_z)) \
                or side_x + side_y <= side_z or side_x + side_z <= side_y or side_y + side_z <= side_x:
            raise ValueError("You can't create a triangle")
        self.side_x = side_x
        self.side_y = side_y
        self.side_z = side_z

    def get_perimeter(self):
        return self.side_x + self.side_y + self.side_z

    def get_semi_perimeter(self):
        return self.get_perimeter() / 2

    def get_area(self):
        return sqrt(self.get_semi_perimeter() * (self.get_semi_perimeter() - self.side_x) *
                    (self.get_semi_perimeter() - self.side_y) * (self.get_semi_perimeter() - self.side_z))
