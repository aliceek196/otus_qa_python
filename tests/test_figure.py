import pytest

from otus_qa_python.src.Circle import Circle
from otus_qa_python.src.Figure import Figure
from otus_qa_python.src.Square import Square


class MockFigure(Figure):
    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0


def test_create_figure():
    figure = MockFigure("TestFigure")
    assert figure.name == "TestFigure"


def test_add_area_valid():
    figure1 = Circle(5)
    other_figure = Square(3)

    expected_result = figure1.get_area() + other_figure.get_area()
    result = figure1.add_area(other_figure)
    assert result == expected_result


def test_add_area_invalid():
    figure = MockFigure("TestFigure")
    with pytest.raises(ValueError):
        figure.add_area("InvalidFigure")
