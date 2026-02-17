# Example 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# Example 2
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

c = Car()
c.start()


# Example 3
class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    pass

s = Student()
s.greet()


# Example 4
class Shape:
    def info(self):
        print("This is a shape")

class Circle(Shape):
    pass

circle = Circle()
circle.info()


# Example 5
class Device:
    def power_on(self):
        print("Device is on")

class Laptop(Device):
    pass

l = Laptop()
l.power_on()
