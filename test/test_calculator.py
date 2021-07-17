import pytest
from simplecalculator import Calculator

calculator= Calculator()

def test_reset():
    assert calculator.reset() == 0

def test_add():
    assert calculator.add(10) == 10

def test_subtract():
    assert calculator.subtract(1) == 9

def test_multiply():
    assert calculator.multiply(3) == 27

def test_divide():
    assert calculator.divide(3) == 9.0
        
def test_nth_root():
    assert calculator.nth_root(3) == 2.1

def test_nth_root_with_num():
    assert calculator.nth_root(3, 27) == 3.0

def test_check_input():
    with pytest.raises(TypeError):
        result= calculator.add("two")

def test_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        result= calculator.divide(0)