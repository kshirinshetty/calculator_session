"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    print("Multiplying:", a, "x", b)
    return a * b

def divide(a, b):
    """Divide a by b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    print("Dividing:", a, "/", b)
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    print("Power:", a, "^", b)
    return a ** b

def square_root(a):
    """Return the square root of a number."""
    if type(a) not in (int, float):
        raise TypeError("Input must be a number")
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    print("Square root of:", a)
    return a ** 0.5

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
