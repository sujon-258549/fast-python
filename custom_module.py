# ============================================
# CUSTOM MODULE - Use Example
# ============================================
# Tomar nijer banano module USE korar example
# my_math.py file ke ekhane import korbo
# ============================================


# ============================================
# 1. IMPORT WAYS - Different methods
# ============================================
print("=== 1. IMPORT METHODS ===")

# Way 1: Import full module
import my_math

print(my_math.add(10, 5))           # 15
print(my_math.PI)                   # 3.14159


# Way 2: Import specific function
from my_math import multiply, square

print(multiply(4, 5))               # 20
print(square(7))                    # 49


# Way 3: Import with alias
import my_math as mm

print(mm.factorial(5))              # 120
print(mm.cube(3))                   # 27


# Way 4: Import multiple specific items
from my_math import add, subtract, PI, E

print(add(100, 200))                # 300
print(subtract(50, 20))             # 30
print(f"PI = {PI}, E = {E}")


# Way 5: Import everything (NOT recommended)
# from my_math import *
# print(divide(10, 2))


# ============================================
# 2. IMPORT CLASS FROM MODULE
# ============================================
print("\n=== 2. IMPORT CLASS ===")

from my_math import Calculator

calc = Calculator()
calc.add(50).subtract(10).add(20).show()    # Result: 60


# ============================================
# 3. EXPLORE MODULE CONTENT
# ============================================
print("\n=== 3. MODULE EXPLORATION ===")

import my_math

# All names in module
print("Module contents:")
for name in dir(my_math):
    if not name.startswith("_"):
        print(f"  - {name}")


# ============================================
# 4. USE MULTIPLE FUNCTIONS
# ============================================
print("\n=== 4. PRACTICAL USAGE ===")

from my_math import add, multiply, square, factorial, is_even

# Simple calculation
result = add(square(3), square(4))    # 9 + 16 = 25
print(f"3^2 + 4^2 = {result}")

# Even/odd check
numbers = [10, 15, 22, 33, 44]
for n in numbers:
    print(f"{n} is {'even' if is_even(n) else 'odd'}")

# Factorial table
print("\nFactorial Table:")
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")


# ============================================
# 5. CREATE YOUR OWN UTILITY MODULE
# ============================================
print("\n=== 5. WHY CUSTOM MODULES? ===")
print("1. Code Reuse - ek code, multiple files e use")
print("2. Organization - related code ek jaygay")
print("3. Maintenance - update ek jaygay korle sob jaygay update")
print("4. Collaboration - team e share kora sohoj")
print("5. Testing - module alada test kora jay")


# ============================================
# HOW TO CREATE YOUR OWN MODULE - 3 STEPS
# ============================================
print("\n=== HOW TO CREATE MODULE ===")
print("Step 1: Create a .py file (e.g., my_module.py)")
print("Step 2: Write functions, classes, variables in it")
print("Step 3: import it in another file")
print("\nExample:")
print("   # my_module.py")
print("   def greet(name):")
print("       return f'Hello {name}!'")
print("")
print("   # main.py")
print("   from my_module import greet")
print("   print(greet('Sujon'))")


# ============================================
# PACKAGE STRUCTURE EXAMPLE
# ============================================
print("\n=== PACKAGE STRUCTURE ===")
print("""
my_package/                  <- package folder
    __init__.py              <- makes it a package
    math_utils.py            <- module 1
    string_utils.py          <- module 2
    data/                    <- sub-package
        __init__.py
        loader.py
        parser.py

Use:
    from my_package import math_utils
    from my_package.data import loader
""")
