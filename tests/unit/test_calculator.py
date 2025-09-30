"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import pytest
from calculator import add, subtract, multiply, divide, power, square_root


class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    def test_multiply_valid(self):
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0

    def test_multiply_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(2, None)

    def test_divide_valid(self):
        assert divide(6, 3) == 2
        assert divide(-6, 2) == -3

    def test_divide_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            divide("10", 2)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            divide(10, "2")

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)

class TestPowerSquareRoot:
    def test_power_valid(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_power_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)

    def test_square_root_valid(self):
        assert square_root(16) == 4
        assert square_root(0) == 0

    def test_square_root_input_validation(self):
        with pytest.raises(TypeError, match="Input must be a number"):
            square_root("9")

    def test_square_root_negative(self):
        with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
            square_root(-4)

