# ============================================
# CUSTOM MODULE - my_math.py
# ============================================
# Eta ekta CUSTOM MODULE - tumi nije banaiyacho
# Onno file e import kore use korte parba:
#   import my_math
#   from my_math import add
# ============================================


# ============================================
# Functions (sob public by default)
# ============================================

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


def square(n):
    """Return square of n"""
    return n * n


def cube(n):
    """Return cube of n"""
    return n * n * n


def is_even(n):
    """Check if number is even"""
    return n % 2 == 0


def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# ============================================
# Variables/Constants (sob accessible)
# ============================================

PI = 3.14159
E = 2.71828
GOLDEN_RATIO = 1.61803


# ============================================
# Class (eta o import kora jay)
# ============================================

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, n):
        self.result += n
        return self

    def subtract(self, n):
        self.result -= n
        return self

    def show(self):
        print(f"Result: {self.result}")
        return self


# ============================================
# __name__ == "__main__" check
# Eta ensure kore ei block SHUDHU direct run hole chole
# Import hole chole na
# ============================================

if __name__ == "__main__":
    # Test code - sudhu direct run hole chole
    print("=== Testing my_math module ===")
    print(f"add(5, 3)      = {add(5, 3)}")
    print(f"subtract(10,4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(20, 4)  = {divide(20, 4)}")
    print(f"square(5)      = {square(5)}")
    print(f"cube(3)        = {cube(3)}")
    print(f"is_even(8)     = {is_even(8)}")
    print(f"factorial(5)   = {factorial(5)}")
    print(f"PI             = {PI}")

    # Class test
    calc = Calculator()
    calc.add(10).subtract(3).add(5).show()    # Result: 12
