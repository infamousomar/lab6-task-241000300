import pytest
from calculator import Calculator

calc = Calculator()


def test_add_positive():
    assert calc.add(2, 3) == 5

def test_add_negative():
    assert calc.add(-2, -3) == -5

def test_add_zero():
    assert calc.add(7, 0) == 7


def test_subtract_positive():
    assert calc.sub(5, 3) == 2

def test_subtract_negative_result():
    assert calc.sub(3, 5) == -2

def test_subtract_zero():
    assert calc.sub(4, 0) == 4


def test_multiply_positive():
    assert calc.mul(3, 4) == 12

def test_multiply_by_zero():
    assert calc.mul(5, 0) == 0

def test_mul_negative():
    assert calc.mul(-3, 4) == -12


def test_div_normal():
    assert calc.div(10, 2) == 5

def test_div_float_result():
    assert calc.div(1, 4) == 0.25

def test_div_by_zero_raises():
    with pytest.raises(ValueError):
        calc.div(5, 0)