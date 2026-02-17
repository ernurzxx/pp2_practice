# Example 1
nums = [5, 2, 9, 1]
print(sorted(nums, key=lambda x: x))

# Example 2
words = ["banana", "apple", "kiwi"]
print(sorted(words, key=lambda w: len(w)))

# Example 3
students = [("Ali", 90), ("Sara", 85)]
print(sorted(students, key=lambda s: s[1]))

# Example 4
nums = [-5, 3, -1]
print(sorted(nums, key=lambda x: abs(x)))

# Example 5
names = ["ali", "Sara", "john"]
print(sorted(names, key=lambda n: n.lower()))
