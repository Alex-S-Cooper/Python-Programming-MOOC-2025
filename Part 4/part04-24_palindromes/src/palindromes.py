# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):
    return word == word[::-1]

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        break
    else:
        print(f"that wasn't a palindrome")
print(f"{word} is a palindrome!")