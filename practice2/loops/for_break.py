#1
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#2
names = ["Ali", "Sara", "John", "Admin"]
for name in names:
    if name == "Admin":
        break
    print(name)

#3
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n > 6:
        break
    print(n)

#4
passwords = ["123", "abc", "admin"]
for p in passwords:
    if p == "admin":
        print("Correct password found")
        break

#5
for i in range(10):
    if i == 8:
        break
    print("Processing:", i)