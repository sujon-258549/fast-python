# ============================================
# Python ENCAPSULATION - Complete Guide
# ============================================
# Encapsulation = Data + Methods ke ek shathe bind kora
# ar baire theke direct access restrict kora
#
# Goal: Data Hiding & Data Protection
# ============================================


# ============================================
# ACCESS MODIFIERS in Python
# ============================================
# 1. Public      -> name        (anywhere accessible)
# 2. Protected   -> _name       (class + subclass only - convention)
# 3. Private     -> __name      (only inside the class)
# ============================================


# ============================================
# 1. PUBLIC MEMBERS
# Baire theke direct access kora jay
# ============================================
print("=== 1. PUBLIC MEMBERS ===")

class Student:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public

s = Student("Sujon", 22)
print(s.name)   # Direct access OK
print(s.age)    # Direct access OK
s.name = "Rahim"  # Direct change OK
print(s.name)


# ============================================
# 2. PROTECTED MEMBERS (single underscore _)
# Convention: baire access korte mana, but technically kora jay
# ============================================
print("\n=== 2. PROTECTED MEMBERS ===")

class Employee:
    def __init__(self, name, salary):
        self.name = name           # public
        self._salary = salary      # protected (warning: don't access outside)

class Manager(Employee):
    def show_salary(self):
        print(f"{self.name}'s salary: {self._salary}")  # subclass e OK

m = Manager("Karim", 50000)
m.show_salary()
print(m._salary)   # Technically kora jay, but bad practice


# ============================================
# 3. PRIVATE MEMBERS (double underscore __)
# Class er baire direct access kora JAY NA
# ============================================
print("\n=== 3. PRIVATE MEMBERS ===")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self.__balance = balance      # private (data hidden!)

    # Getter method - balance dekhar jonno
    def get_balance(self):
        return self.__balance

    # Setter method - balance change korar jonno (with validation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount!")

account = BankAccount("Sujon", 1000)
print(account.owner)              # public - OK
print(account.get_balance())      # 1000 (via method)

account.deposit(500)
print(account.get_balance())      # 1500

account.withdraw(2000)            # Insufficient!
account.withdraw(300)
print(account.get_balance())      # 1200

# Direct access try korle ERROR
# print(account.__balance)        # AttributeError!


# ============================================
# 4. NAME MANGLING
# Private variable internally renamed hoy: _ClassName__variable
# ============================================
print("\n=== 4. NAME MANGLING ===")

# Backdoor diye access kora jay (but BAD practice)
print(account._BankAccount__balance)   # 1200 (name mangled)


# ============================================
# 5. GETTER & SETTER METHODS
# Private data access korar standard way
# ============================================
print("\n=== 5. GETTER & SETTER ===")

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter (with validation)
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")

    def set_age(self, age):
        if 0 < age < 150:
            self.__age = age
        else:
            print("Invalid age!")

p = Person("Sujon", 22)
print(p.get_name(), p.get_age())

p.set_age(25)
p.set_age(-5)        # validation reject
print(p.get_age())   # 25


# ============================================
# 6. @property DECORATOR (Pythonic way)
# Method ke variable er moto access kora jay
# ============================================
print("\n=== 6. @property DECORATOR ===")

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        """Getter"""
        return self.__price

    @price.setter
    def price(self, value):
        """Setter with validation"""
        if value < 0:
            print("Price cannot be negative!")
        else:
            self.__price = value

    @price.deleter
    def price(self):
        """Deleter"""
        print("Price deleted")
        del self.__price

item = Product("Laptop", 50000)
print(item.price)        # Getter - 50000 (method, but used like variable)

item.price = 55000       # Setter
print(item.price)        # 55000

item.price = -100        # Validation kicks in
print(item.price)        # Still 55000

# del item.price         # Deleter


# ============================================
# 7. REAL WORLD EXAMPLE - ATM System
# ============================================
print("\n=== 7. REAL WORLD: ATM ===")

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin              # private - secret!
        self.__balance = balance      # private

    def __verify_pin(self, entered_pin):   # private method
        return entered_pin == self.__pin

    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Balance: {self.__balance}"
        return "Wrong PIN!"

    def withdraw(self, pin, amount):
        if not self.__verify_pin(pin):
            return "Wrong PIN!"
        if amount > self.__balance:
            return "Insufficient balance!"
        self.__balance -= amount
        return f"Withdrawn {amount}. Remaining: {self.__balance}"

atm = ATM(1234, 10000)
print(atm.check_balance(1234))
print(atm.check_balance(9999))     # Wrong PIN
print(atm.withdraw(1234, 3000))
print(atm.withdraw(1234, 50000))   # Insufficient


# ============================================
# Encapsulation Summary
# ============================================
print("\n=== Encapsulation Benefits ===")
print("1. Data Hiding - private data safe")
print("2. Data Protection - validation through setter")
print("3. Flexibility - internal change without affecting outside")
print("4. Security - direct access blocked")
print("5. Maintainability - code organize and clean")
