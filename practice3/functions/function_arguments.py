# Example 1
def introduce(name, age):
    print(f"{name} is {age} years old")

introduce("Sara", 20)

# Example 2
introduce(age=25, name="John")

# Example 3
def country(name, country="USA"):
    print(name, "is from", country)

country("Alex")
country("Maria", "Spain")

# Example 4
def multiply(a, b=2):
    print(a * b)

multiply(5)
multiply(5, 3)

# Example 5
def greet_user(name="Guest"):
    print("Hello", name)

greet_user()
