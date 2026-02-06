#1
count = 1
while count <= 5:
    print(count)
    count += 1

#2
password = ""
while password != "admin":
    password = input("Enter password: ")
print("Access granted")

#3
fuel = 10
while fuel > 0:
    print("Driving... fuel left:", fuel)
    fuel -= 2

#4
temperature = 25
while temperature > 20:
    print("Cooling down:", temperature)
    temperature -= 1


#5
tries = 3
while tries > 0:
    print("Attempts left:", tries)
    tries -= 1