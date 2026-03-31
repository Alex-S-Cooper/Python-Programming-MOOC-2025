def found(vowel, user_str):
    if vowel in user_str:
        return f"{vowel} found"
    else:
        return f"{vowel} not found"

user_str = input("Please type in a string: ")
print(found("a", user_str))
print(found("e", user_str))
print(found("o", user_str))

