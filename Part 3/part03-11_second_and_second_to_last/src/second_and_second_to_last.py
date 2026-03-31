user_input = input("Please type in a string: ")
second_chr = user_input[1]
second_to_last_chr = user_input[-2]

if second_chr == second_to_last_chr:
    print(f"The second and the second to last characters are {second_chr}")
else:
    print("The second and the second to last characters are different")