import pytest
from otus_qa_python.src.Figure import Figure


class MockFigure(Figure):
    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0


def test_create_figure():
    figure = MockFigure("TestFigure")
    assert figure.name == "TestFigure"


def test_add_area_valid():
    figure1 = MockFigure("Figure1")
    figure2 = MockFigure("Figure2")

    figure1.add_area = 1
    figure2.add_area = 2

    result = figure1.add_area + figure2.add_area
    assert result == 3


def test_add_area_invalid():
    figure = MockFigure("TestFigure")
    with pytest.raises(ValueError):
        figure.add_area("InvalidFigure")
