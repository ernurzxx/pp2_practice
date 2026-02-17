# Example 1
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

Child().skills()


# Example 2
class Writer:
    def write(self):
        print("Writing book")

class Speaker:
    def speak(self):
        print("Public speaking")

class Author(Writer, Speaker):
    pass

a = Author()
a.write()
a.speak()


# Example 3
class Fly:
    def move(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

d = Duck()
d.move()
d.swim()


# Example 4
class Teacher:
    def teach(self):
        print("Teaching")

class Researcher:
    def research(self):
        print("Researching")

class Professor(Teacher, Researcher):
    pass

p = Professor()
p.teach()
p.research()


# Example 5
class Camera:
    def take_photo(self):
        print("Taking photo")

class Phone:
    def call(self):
        print("Making call")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.call()
