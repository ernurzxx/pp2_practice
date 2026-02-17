# Example 1
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ali")
print(p1.name)

# Example 2
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.brand)

# Example 3
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Sara", "A")
print(s1.name, s1.grade)

# Example 4
class Circle:
    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)
print(c1.radius)

# Example 5
class Laptop:
    def __init__(self, model):
        self.model = model
