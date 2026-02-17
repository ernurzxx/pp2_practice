# Example 1
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

# Example 2
names = ["ali", "sara"]
upper_names = list(map(lambda n: n.upper(), names))
print(upper_names)

# Example 3
nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums))
print(doubled)

# Example 4
nums = [10, 20, 30]
half = list(map(lambda x: x/2, nums))
print(half)

# Example 5
words = ["hi", "hello"]
lengths = list(map(lambda w: len(w), words))
print(lengths)
