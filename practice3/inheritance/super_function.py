# Example 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s1 = Student("Ali", "A")
print(s1.name, s1.grade)


# Example 2
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

d1 = Dog("Canine", "Labrador")
print(d1.species, d1.breed)


# Example 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c1 = Car("Toyota", "Corolla")
print(c1.brand, c1.model)


# Example 4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m1 = Manager("Sara", 5000, "IT")
print(m1.name, m1.salary, m1.department)


# Example 5
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle1 = Circle("Red", 10)
print(circle1.color, circle1.radius)
