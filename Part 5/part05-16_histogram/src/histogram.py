# Write your solution here
def histogram(string):
    letter_count = {}
    for letter in string:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    for letter in letter_count:
        print(f"{letter} {"*" * letter_count[letter]}")