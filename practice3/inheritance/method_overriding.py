# Example 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

Dog().speak()


# Example 2
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting with key")

Car().start()


# Example 3
class Person:
    def greet(self):
        print("Hello!")

class Teacher(Person):
    def greet(self):
        print("Good morning students!")

Teacher().greet()


# Example 4
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

Circle().draw()


# Example 5
class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def work(self):
        print("Manager managing team")

Manager().work()
