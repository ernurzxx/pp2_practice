# Example 1
def add_numbers(*args):
    print(sum(args))

add_numbers(1, 2, 3, 4)

# Example 2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Ali", age=22)

# Example 3
def show_details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_details(1, 2, name="Sara")

# Example 4
def multiply_all(*nums):
    result = 1
    for n in nums:
        result *= n
    print(result)

multiply_all(2, 3, 4)

# Example 5
def greet(**data):
    print("Hello", data.get("name", "Guest"))

greet(name="Ahmad")
