from app.operations import addition, division, multiplication, subtraction
import pytest

def test_addtion():
    assert addition(2,3) == 5
    assert addition(-2,3) == 1

def test_subtraction():
    assert subtraction(5,3) == 2
    assert subtraction(5,-3) == 8

def test_multiplication():
    assert multiplication(2,3) == 6
    assert multiplication(-2,3) == -6

def test_division():
    assert division(6,3) == 2

def test_division_with_zero():
    # this is negative test designed to fail
    # division by zero should raise an error
    with pytest.raises(ZeroDivisionError):
        division(6, 0)