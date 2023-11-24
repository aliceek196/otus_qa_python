import pytest
from otus_qa_python.src.Rectangle import Rectangle


@pytest.mark.parametrize(("side_x", "side_y", "perimeter", "area"),
                         [
                             (4, 6, 20, 24),
                             (3.6, 5.7, 18.6, 20.52),
                             (7, 7, 28, 49),
                             (1000, 3000, 8000, 3000000)
                         ], ids=["integer_sides", "decimal_sides", "equal_sides", "large_sides"])
def test_rectangle_valid(side_x, side_y, perimeter, area):
    r = Rectangle(side_x, side_y)
    assert r.get_perimeter() == perimeter
    assert r.get_area() == area


@pytest.mark.parametrize(("side_x", "side_y", "expected_exception"),
                         [
                            (-3, 4, ValueError),
                            (5, -6, ValueError),
                            (0, 10, ValueError),
                            (3, 0, ValueError),
                            ("one", "two", ValueError)
                        ], ids=["x_negative_side", "y_negative_side", "x_is_zero", "y_is_zero", "string_sides"])
def test_rectangle_invalid(side_x, side_y, expected_exception):
    with pytest.raises(expected_exception):
        Rectangle(side_x, side_y)
