import pytest
import math

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Figure import Figure


@pytest.mark.parametrize("value", [0, -1])
def test_circle_area_negative(value):
    with pytest.raises(ValueError):
        Circle(r=value).area


@pytest.mark.parametrize("value", [0, -1])
def test_circle_perimeter_negative(value):
    with pytest.raises(ValueError):
        Circle(r=value).perimeter


def test_circle_area():
    _r = 7
    assert Circle(_r).area == math.pi * math.pow(_r, 2)


def test_circle_perimeter():
    _r = 7
    assert Circle(_r).perimeter == 2 * math.pi * _r


def test_circle_add_area():
    _r = 7
    _a = 2
    _b = 3
    _c = 4
    assert Circle(_r).add_area(Rectangle(_a, _b)) == Rectangle(_a, _b).add_area(Circle(_r))


def test_circle_add_area_negative():
    _r = 7
    _obj = Figure()
    with pytest.raises(ValueError):
        Circle(_r).add_area(_obj)



