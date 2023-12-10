import pytest
from otus_qa_python.src.Rectangle import Rectangle


@pytest.mark.parametrize(("side_x", "side_y", "perimeter", "area"),
                         [
                             (4, 6, 20, 24),
                             (3.6, 5.7, 18.6, 20.52),
                         ], ids=["integer_sides", "decimal_sides"])
def test_rectangle_valid(side_x, side_y, perimeter, area):
    r = Rectangle(side_x, side_y)
    assert r.get_perimeter() == perimeter
    assert r.get_area() == area


@pytest.mark.parametrize(("side_x", "side_y"),
                         [
                            (-3, 4),
                            (5, -6),
                            (0, 10),
                            (3, 0),
                            ("one", "two")
                        ], ids=["x_negative_side", "y_negative_side", "x_is_zero", "y_is_zero", "string_sides"])
def test_rectangle_invalid(side_x, side_y):
    with pytest.raises(ValueError):
        Rectangle(side_x, side_y)
