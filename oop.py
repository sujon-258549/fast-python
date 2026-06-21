
# dunder methods

# constructors 3 type
#   defult constructor
#  parameterized constructor
#   defult value constructor


#   defult constructor

class person19:
    def __init__(self):
        self.name = ""
        self.age = 0

p=person19()
p.name="Md Sujon Mia"
p.age=10

# print(p.name)


#   defult value constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 36)
person2 = Person("Jane", 28)

# print(person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)



class Person11:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# p1 = Person11("Sujon", 22)

# print("Name:", p1.name)
# print("Age:", p1.age)



class School :

   school_name = "Sujon School"
   def __init__(self, name):
        self.school_name = name


s1 = School("Sujon School")
s2 = School("Sujon School")

print(s1.school_name)
print(s2.school_name)