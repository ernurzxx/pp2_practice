#1
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

#2
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print("Odd number:", count)

#3
fuel = 5
while fuel > 0:
    fuel -= 1
    if fuel == 2:
        continue
    print("Fuel level:", fuel)

#4
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print("Step", i)

#5
tries = 5
while tries > 0:
    tries -= 1
    if tries == 1:
        continue
    print("Tries left:", tries)