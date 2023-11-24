import pytest
from otus_qa_python.src.Triangle import Triangle


@pytest.mark.parametrize(("side_x", "side_y", "side_z"), [
    (3, 4, 5),
    (3, 3, 3),
    (4, 4, 5),
    (2, 3, 6),
    (0, 4, 5),
    (10, -4, 5),
    (3, 4, "a"),
], ids=["valid_triangle", "valid_equilateral_triangle", "valid_isosceles_triangle", "invalid_triangle_of_sum_sides",
        "invalid_triangle_x_is_zero", "invalid_triangle_y_is_negative", "invalid_triangle_z_is_string"])
def test_create_triangle(side_x, side_y, side_z):
    if side_x + side_y <= side_z or side_x + side_z <= side_y or side_y + side_z <= side_x or \
            any(side <= 0 for side in (side_x, side_y, side_z)):
        with pytest.raises(ValueError):
            Triangle(side_x, side_y, side_z)
    else:
        tr = Triangle(side_x, side_y, side_z)
        assert tr.side_x == side_x
        assert tr.side_y == side_y
        assert tr.side_z == side_z


def test_triangle_perimeter(triangle_sides):
    assert triangle_sides.get_perimeter() == 12


def test_triangle_semi_perimeter(triangle_sides):
    assert triangle_sides.get_semi_perimeter() == 6


def test_triangle_area(triangle_sides):
    assert triangle_sides.get_area() == 6.0
