import pytest
from tools.calculator import Calculator

def test_addition():
    assert Calculator().calculate(2, "+", 3) == 5

def test_unknown_operation():
    with pytest.raises(ValueError):
        Calculator().calculate(2, "^", 3)

def test_division_by_zero():
    with pytest.raises(ValueError):
        Calculator().calculate(2, "/", 0)
