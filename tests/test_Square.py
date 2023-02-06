import pytest

from src.Figure import Figure
from src.Square import Square
from src.Circle import Circle


@pytest.mark.parametrize("value_a", [-1, 0])
def test_rectangle_area_negative(value_a):
    with pytest.raises(ValueError):
        Square(a=value_a).area


@pytest.mark.parametrize("value_a", [-1, 0])
def test_rectangle_perimeter_negative(value_a):
    with pytest.raises(ValueError):
        Square(a=value_a).perimeter


def test_square_area():
    _a = 7
    assert Square(_a).area == _a*_a


def test_square_perimeter():
    _a = 2
    assert Square(_a).perimeter == 4 * _a


def test_square_add_area():
    _a = 2
    _r = 5
    assert Square(_a).add_area(Circle(_r)) == Circle(_r).add_area(Square(_a))


def test_square_add_area_negative():
    _a = 7
    _obj = Figure()
    with pytest.raises(ValueError):
        Square(_a).add_area(_obj)

