print("Please type in integer numbers. Type in 0 to finish.")
num_of_nums = 0
sum_of_nums = 0
positive_nums = 0
negative_nums = 0
while True:
    number = int(input("Number: "))

    if number == 0:
        break

    if number > 0:
        positive_nums += 1
    if number < 0:
        negative_nums += 1

    num_of_nums += 1
    sum_of_nums += number
print(f"Numbers typed in {num_of_nums}")
print(f"The sum of the numbers is {sum_of_nums}")
print(f"The mean of the numbers is {sum_of_nums / num_of_nums}")
print(f"Positive numbers {positive_nums}")
print(f"Negative numbers {negative_nums}")