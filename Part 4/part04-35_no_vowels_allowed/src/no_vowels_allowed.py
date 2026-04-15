# Write your solution here
def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for letter in string:
        if letter not in vowels:
            new_string += letter
    return new_string