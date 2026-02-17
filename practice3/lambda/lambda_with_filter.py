# Example 1
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Example 2
nums = [10, 15, 20]
greater_than_15 = list(filter(lambda x: x > 15, nums))
print(greater_than_15)

# Example 3
names = ["Ali", "Sara", "John"]
short_names = list(filter(lambda n: len(n) <= 4, names))
print(short_names)

# Example 4
nums = [-2, 3, -1, 5]
positive = list(filter(lambda x: x > 0, nums))
print(positive)

# Example 5
words = ["apple", "", "banana"]
non_empty = list(filter(lambda w: w != "", words))
print(non_empty)
