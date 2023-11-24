from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("You can't add the area of a figure")
        return self.add_area() + other_figure.add_area()