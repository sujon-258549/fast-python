# ============================================
# Python POLYMORPHISM - Complete Guide
# ============================================
# "Poly" = Many, "Morph" = Form
# Polymorphism = One name, many forms
# Same function/method works differently with different objects
# ============================================


# ============================================
# 1. BUILT-IN POLYMORPHISM
# Same function works on different data types
# ============================================
print("=== 1. BUILT-IN POLYMORPHISM ===")

# len() works on string, list, tuple, dict
print(len("Hello"))           # 5  (string)
print(len([1, 2, 3, 4]))      # 4  (list)
print(len((1, 2, 3)))         # 3  (tuple)
print(len({"a": 1, "b": 2}))  # 2  (dictionary)

# + operator works differently
print(5 + 3)                  # 8       (addition)
print("Hello " + "World")     # Hello World (concatenation)
print([1, 2] + [3, 4])        # [1, 2, 3, 4] (list merge)


# ============================================
# 2. METHOD OVERRIDING (Inheritance based)
# Child class overrides parent's method
# ============================================
print("\n=== 2. METHOD OVERRIDING ===")

class Animal:
    def sound(self):
        print("Animals make some sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Ghew Ghew")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")

class Cow(Animal):
    def sound(self):
        print("Cow says: Hamba")

# Same method name, different behavior
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()


# ============================================
# 3. POLYMORPHISM WITH FUNCTIONS
# Same function works with different objects
# ============================================
print("\n=== 3. FUNCTION POLYMORPHISM ===")

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

def print_area(shape):
    print(f"Area: {shape.area()}")

print_area(Circle(5))
print_area(Square(4))
print_area(Rectangle(6, 3))


# ============================================
# 4. METHOD OVERLOADING (Python style)
# Python e direct overloading nai, default argument diye kora hoy
# ============================================
print("\n=== 4. METHOD OVERLOADING (Default Args) ===")

class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d

calc = Calculator()
print(calc.add(2, 3))           # 5
print(calc.add(2, 3, 4))        # 9
print(calc.add(2, 3, 4, 5))     # 14


# ============================================
# 5. OPERATOR OVERLOADING
# Built-in operators (+, -, *) work for custom objects
# ============================================
print("\n=== 5. OPERATOR OVERLOADING ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # + operator overload
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # - operator overload
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # str() representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(5, 7)

print(p1 + p2)   # Point(7, 10)
print(p2 - p1)   # Point(3, 4)


# ============================================
# 6. DUCK TYPING (Python special feature)
# "If it walks like a duck and quacks like a duck, it's a duck"
# Type matter na, behavior matter
# ============================================
print("\n=== 6. DUCK TYPING ===")

class Duck:
    def speak(self):
        print("Quack Quack")

class Human:
    def speak(self):
        print("Hello, I am human")

class Robot:
    def speak(self):
        print("Beep Boop, I am robot")

def make_it_speak(obj):
    obj.speak()    # type check kore na, just method call kore

make_it_speak(Duck())
make_it_speak(Human())
make_it_speak(Robot())


print("\n=== Polymorphism Summary ===")
print("1. Built-in: len(), +, * etc work with different types")
print("2. Method Overriding: Child class redefines parent method")
print("3. Function Polymorphism: One function, many object types")
print("4. Method Overloading: Default arguments")
print("5. Operator Overloading: __add__, __sub__ etc")
print("6. Duck Typing: Behavior > Type")
