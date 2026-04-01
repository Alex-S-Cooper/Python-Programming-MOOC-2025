number = int(input("Please type in a number: "))

i = 1
while i <= number:
    if i == number and number % 2 != 0:
        print(number)
    elif i % 2 != 0:
        print(i + 1)
    elif i % 2 == 0:
        print(i - 1)
    i += 1
   

