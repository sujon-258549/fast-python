class Student:

    def __init__(self, name):
        self.__name = name

    # Getter
    @property
    def name(self):
        return self.__name

    # Setter
    @name.setter
    def name(self, value):
        self.__name = value


s1 = Student("Sujon")

# Getter call
print(s1.name)

# Setter call
s1.name = "Rahim"

print(s1.name)