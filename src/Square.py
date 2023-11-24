from otus_qa_python.src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_x):
        if side_x <= 0:
            raise ValueError("You can't create a square")
        super().__init__(side_x, side_x)
