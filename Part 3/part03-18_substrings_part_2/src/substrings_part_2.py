user_str = input("Please type in a string: ")

i = len(user_str) - 1
while i >= 0:
    print(user_str[i:len(user_str)])
    i -= 1