# ============================================
# MODULE AND PACKAGE INTRODUCTION
# ============================================
# MODULE  = ekta .py file (jeta onno file e import kora jay)
# PACKAGE = onek module er ekta folder (__init__.py thake)
#
# Benefits: Code reuse, organization, namespace
# ============================================


# ============================================
# 1. WHAT IS A MODULE?
# ============================================
# Module = ek ta Python file (.py)
# Example: math, random, os - sob module
#
# Tomar nijer banano file o module
# ============================================
print("=== 1. MODULE INTRODUCTION ===")

# Built-in module import
import math

print(math.pi)              # 3.141592...
print(math.sqrt(25))        # 5.0
print(math.factorial(5))    # 120


# ============================================
# 2. DIFFERENT WAYS TO IMPORT
# ============================================
print("\n=== 2. IMPORT METHODS ===")

# Way 1: Import full module
import math
print(math.sqrt(16))

# Way 2: Import specific function
from math import sqrt, pi
print(sqrt(36))
print(pi)

# Way 3: Import with alias (nickname)
import math as m
print(m.sqrt(49))

# Way 4: Import all (NOT recommended - namespace pollution)
# from math import *
# print(sqrt(64))

# Way 5: Import specific with alias
from math import factorial as fact
print(fact(6))


# ============================================
# 3. BUILT-IN MODULES (Popular ones)
# ============================================
print("\n=== 3. BUILT-IN MODULES ===")

import math
import random
import datetime
import os
import sys

print("math.pi:", math.pi)
print("random:", random.randint(1, 10))
print("today:", datetime.date.today())
print("cwd:", os.getcwd())
print("python version:", sys.version[:6])


# ============================================
# 4. WHAT IS A PACKAGE?
# ============================================
# Package = folder with multiple modules + __init__.py file
#
# Structure example:
#   mypackage/
#       __init__.py
#       module1.py
#       module2.py
#       subpackage/
#           __init__.py
#           module3.py
#
# Use: from mypackage import module1
#      from mypackage.subpackage import module3
# ============================================
print("\n=== 4. PACKAGE STRUCTURE ===")
print("Package = folder with __init__.py")
print("Example: numpy, pandas, requests - all packages")


# ============================================
# 5. dir() AND help()
# Module er moddhe ki ki ache dekho
# ============================================
print("\n=== 5. EXPLORING MODULES ===")

import math
# print(dir(math))           # all functions/variables in math
# help(math.sqrt)            # documentation of sqrt

print("math module has:", len(dir(math)), "items")


# ============================================
# 6. __name__ AND __main__
# Script direct run hocche na import hocche bujhar way
# ============================================
print("\n=== 6. __name__ AND __main__ ===")

print("Current __name__:", __name__)

if __name__ == "__main__":
    print("This file is being RUN directly")
else:
    print("This file is being IMPORTED")


# ============================================
# 7. INSTALLING EXTERNAL PACKAGES
# ============================================
# Terminal e:
#   pip install package_name
#   pip install requests
#   pip install numpy pandas
#
# Check installed: pip list
# Uninstall:       pip uninstall package_name
# ============================================
print("\n=== 7. PIP COMMANDS ===")
print("Install:   pip install <package>")
print("List:      pip list")
print("Uninstall: pip uninstall <package>")
print("Upgrade:   pip install --upgrade <package>")


# ============================================
# SUMMARY
# ============================================
print("\n=== SUMMARY ===")
print("MODULE  = single .py file")
print("PACKAGE = folder of modules (with __init__.py)")
print("Use 'import' to load module")
print("Use 'from X import Y' to load specific item")
print("Use 'as' for alias")
