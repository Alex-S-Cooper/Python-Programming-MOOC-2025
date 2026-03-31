word = input("Please type in a word: ")
start = input("Please type in a character: ")
index = 0
while index < len(word):
    if word[index] == start:
        substring = word[index:index + 3]
        if len(substring) >= 3:
            print(substring)
    index += 1


