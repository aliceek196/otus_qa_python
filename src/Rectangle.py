from otus_qa_python.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_x, side_y):
        super().__init__(name="Rectangle")
        if any(side <= 0 for side in (side_x, side_y)):
            raise ValueError("You can't create a rectangle")
        self.side_x = side_x
        self.side_y = side_y

    def get_perimeter(self):
        return 2 * (self.side_x + self.side_y)

    def get_area(self):
        return self.side_x * self.side_y
