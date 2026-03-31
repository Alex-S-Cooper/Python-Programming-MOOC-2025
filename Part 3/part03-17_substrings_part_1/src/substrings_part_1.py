user_str = input("Please type in a string: ")

i = 1
while i <= len(user_str):
    print(user_str[:i])
    i += 1