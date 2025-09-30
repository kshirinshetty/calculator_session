"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from calculator import add, subtract, multiply, divide, power, square_root

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide two numbers with input validation."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b with validation."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both arguments must be numbers")
    return a ** b

def square_root(a):
    """Return the square root of a number with validation."""
    if type(a) not in (int, float):
        raise TypeError("Input must be a number")
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a ** 0.5

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
