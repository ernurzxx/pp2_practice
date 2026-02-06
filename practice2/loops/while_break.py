#1
count = 1
while True:
    print(count)
    if count == 5:
        break
    count += 1

#2
while True:
    command = input("Type 'exit' to quit: ")
    if command == "exit":
        break

#3
balance = 1000
while balance > 0:
    print("Balance:", balance)
    if balance == 500:
        break
    balance -= 100

#4
number = 1
while number <= 10:
    if number == 7:
        break
    print(number)
    number += 1

#5
attempts = 5
while attempts > 0:
    if attempts == 2:
        print("Too many failed attempts")
        break
    attempts -= 1