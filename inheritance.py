# ============================================
# Python Inheritance - All Types
# ============================================


# ============================================
# 1. SINGLE INHERITANCE
# One child class inherits from one parent class
# ============================================
print("=== SINGLE INHERITANCE ===")

class GrandFather:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Father(GrandFather):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

father = Father("Sujon", 50, "Engineer")
print(father.name)        # Output: Sujon
print(father.age)         # Output: 50
print(father.profession)  # Output: Engineer


# ============================================
# 2. MULTIPLE INHERITANCE
# One child class inherits from multiple parent classes
# ============================================
print("\n=== MULTIPLE INHERITANCE ===")

class Father2:
    def __init__(self, father_name):
        self.father_name = father_name
    def skill_from_father(self):
        print("Father gave: Hard working skill")

class Mother2:
    def __init__(self, mother_name):
        self.mother_name = mother_name
    def skill_from_mother(self):
        print("Mother gave: Cooking skill")

class Child(Father2, Mother2):
    def __init__(self, father_name, mother_name, child_name):
        Father2.__init__(self, father_name)
        Mother2.__init__(self, mother_name)
        self.child_name = child_name

child = Child("Karim", "Rahima", "Sujon")
print("Father:", child.father_name)
print("Mother:", child.mother_name)
print("Child:", child.child_name)
child.skill_from_father()
child.skill_from_mother()


# ============================================
# 3. MULTILEVEL INHERITANCE
# Parent -> Child -> GrandChild (chain)
# ============================================
print("\n=== MULTILEVEL INHERITANCE ===")

class Grandfather3:
    def __init__(self, surname):
        self.surname = surname
    def show_surname(self):
        print("Surname:", self.surname)

class Father3(Grandfather3):
    def __init__(self, surname, profession):
        super().__init__(surname)
        self.profession = profession
    def show_profession(self):
        print("Profession:", self.profession)

class Son3(Father3):
    def __init__(self, surname, profession, name):
        super().__init__(surname, profession)
        self.name = name
    def show_name(self):
        print("Name:", self.name)

son = Son3("Ahmed", "Doctor", "Sujon")
son.show_surname()      # from Grandfather
son.show_profession()   # from Father
son.show_name()         # own method


# ============================================
# 4. HIERARCHICAL INHERITANCE
# One parent -> Multiple children
# ============================================
print("\n=== HIERARCHICAL INHERITANCE ===")

class Parent:
    def __init__(self, surname):
        self.surname = surname
    def family_name(self):
        print("Family:", self.surname)

class Son(Parent):
    def role(self):
        print("I am the son")

class Daughter(Parent):
    def role(self):
        print("I am the daughter")

s = Son("Khan")
d = Daughter("Khan")
s.family_name()
s.role()
d.family_name()
d.role()


# ============================================
# 5. HYBRID INHERITANCE
# Mix of two or more types (multiple + multilevel)
# ============================================
print("\n=== HYBRID INHERITANCE ===")

class A:
    def method_a(self):
        print("Method from class A")

class B(A):
    def method_b(self):
        print("Method from class B")

class C(A):
    def method_c(self):
        print("Method from class C")

class D(B, C):
    def method_d(self):
        print("Method from class D")

obj = D()
obj.method_a()    # from A
obj.method_b()    # from B
obj.method_c()    # from C
obj.method_d()    # from D

print("\nMRO (Method Resolution Order):")
print(D.__mro__)
