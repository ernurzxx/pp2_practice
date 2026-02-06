#1
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        continue
    print("Odd:", n)

#3
names = ["Ali", "", "Sara", ""]
for name in names:
    if name == "":
        continue
    print("Name:", name)

#4
for i in range(10):
    if i < 5:
        continue
    print(i)

#5
prices = [100, -1, 200, -1, 300]
for price in prices:
    if price == -1:
        continue
    print("Price:", price)