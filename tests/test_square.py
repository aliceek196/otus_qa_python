import pytest
from otus_qa_python.src.Square import Square


@pytest.mark.parametrize(("side_x", "perimeter", "area"),
                         [
                             (4, 16, 16),
                             (1.2, 4.8, 1.44),
                             (1000, 4000, 1000000)
                         ], ids=["integer_side", "decimal_side", "large_side"])
def test_rectangle_valid(side_x, perimeter, area):
    s = Square(side_x)
    assert s.get_perimeter() == perimeter
    assert s.get_area() == area


@pytest.mark.parametrize(("side_x", "expected_exception"),
                         [
                             (-3, ValueError),
                             (0, ValueError),
                             ("one", ValueError)
                         ], ids=["negative_side", "zero_side", "string_side"])
def test_square_invalid(side_x, expected_exception):
    with pytest.raises(expected_exception):
        Square(side_x)
