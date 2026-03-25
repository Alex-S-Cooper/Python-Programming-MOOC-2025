from math import sqrt

while True:
    num = int(input("Please type in a number: "))

    if num < 0:
        print("Invalid number")
    if num > 0:
        print(sqrt(num))
    if num == 0:
        break
print("Exiting...")