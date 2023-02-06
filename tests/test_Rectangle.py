import pytest


from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Figure import Figure


@pytest.mark.parametrize("value_a, value_b", [(-1, 0), (0, -1)])
def test_rectangle_area_negative(value_a, value_b):
    with pytest.raises(ValueError):
        Rectangle(a=value_a, b=value_b).area


@pytest.mark.parametrize("value_a, value_b", [(-1, -1), (0, 0)])
def test_rectangle_perimeter_negative(value_a, value_b):
    with pytest.raises(ValueError):
        Rectangle(a=value_a, b=value_b).perimeter


def test_rectangle_area():
    _a = 7
    _b = 2
    assert Rectangle(_a, _b).area == _a*_b


def test_rectangle_perimeter():
    _a = 7
    _b = 2
    assert Rectangle(_a, _b).perimeter == 2 * (_a + _b)


def test_rectangle_add_area():
    _a = 2
    _b = 3
    _aa = 13
    _bb = 14
    _cc = 15
    assert Rectangle(_a, _b).add_area(Triangle(_aa, _bb, _cc)) == Triangle(_aa, _bb, _cc).add_area(Rectangle(_a, _b))


def test_rectangle_add_area_negative():
    _a = 7
    _b = 5
    _obj = Figure()
    with pytest.raises(ValueError):
        Rectangle(_a, _b).add_area(_obj)