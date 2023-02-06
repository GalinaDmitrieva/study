import pytest
import math


from src.Triangle import Triangle
from src.Figure import Figure
from src.Square import Square


@pytest.mark.parametrize("value_a, value_b, value_c",
                         [(-1, 0, 1),
                          (0, -1, 1),
                          (1, 1, 0),
                          (1, 2, 3)])
def test_triangle_area_negative(value_a, value_b, value_c):
    with pytest.raises(ValueError):
        Triangle(a=value_a, b=value_b, c=value_c).area


@pytest.mark.parametrize("value_a, value_b, value_c",
                         [(-1, 0, 1),
                          (0, -1, 1),
                          (1, 1, 0),
                          (1, 2, 3)])
def test_triangle_perimeter_negative(value_a, value_b, value_c):
    with pytest.raises(ValueError):
        Triangle(a=value_a, b=value_b, c=value_c).perimeter


def test_triangle_area():
    _aa = 12
    _bb = 13
    _cc = 14
    assert Triangle(_aa, _bb, _cc).area == math.sqrt(((_aa+_bb+_cc)/2) *
                                                  (((_aa+_bb+_cc)/2) - _aa) *
                                                  (((_aa+_bb+_cc)/2) - _bb) *
                                                  (((_aa+_bb+_cc)/2) - _cc))


def test_triangle_perimeter():
    _aa = 13
    _bb = 14
    _cc = 15
    assert Triangle(_aa, _bb, _cc).perimeter == (_aa + _bb + _cc)


def test_triangle_add_area():
    _aa = 13
    _bb = 14
    _cc = 15
    _a = 2
    assert Triangle(_aa, _bb, _cc).add_area(Square(_a)) == Square(_a).add_area(Triangle(_aa, _bb, _cc))


def test_triangle_add_area_negative():
    _aa = 7
    _bb = 5
    _cc = 6
    _obj = Figure()
    with pytest.raises(ValueError):
        Triangle(_aa, _bb, _cc).add_area(_obj)

