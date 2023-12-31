from math import pi
import pytest
from otus_qa_python.src.Circle import Circle


def test_circle_valid_perimeter(circle_positive):
    expected_perimeter = 2 * pi * circle_positive.radius
    assert circle_positive.get_perimeter() == expected_perimeter


def test_circle_valid_area(circle_positive):
    expected_area = pi * circle_positive.radius * circle_positive.radius
    assert circle_positive.get_area() == expected_area


@pytest.mark.parametrize("radius",
                         [
                             (-3),
                             0,
                             "five"
                         ], ids=["negative_radius", "zero_radius", "string_radius"])
def test_circle_invalid(radius):
    with pytest.raises(ValueError):
        Circle(radius)
