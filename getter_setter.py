class Student:

    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age

    # Getter Method
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter Method
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


s1 = Student("Sujon", 22)

# Getter
print(s1.get_name())
print(s1.get_age())

# Setter
s1.set_name("Rahim")
s1.set_age(25)

print(s1.get_name())
print(s1.get_age())