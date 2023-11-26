import pytest
from otus_qa_python.src.Circle import Circle
from otus_qa_python.src.Triangle import Triangle
from contextlib import contextmanager


@pytest.fixture
def circle_positive():
    radius = 5
    return Circle(radius)


@pytest.fixture
def triangle_sides():
    side_x = 3
    side_y = 4
    side_z = 5
    return Triangle(side_x, side_y, side_z)


@contextmanager
def does_not_raise():
    yield
