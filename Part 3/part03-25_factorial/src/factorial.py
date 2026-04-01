while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    i = 1
    sum = 1
    while i <= number:
        sum *= i
        i += 1
    print(f"The factorial of the number {number} is {sum}")
print("Thanks and bye!")