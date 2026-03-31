word = input("Please type in a word: ")
start = input("Please type in a character: ")
start_index = word.find(start)
word_slice = word[start_index:start_index + 3]
if len(word_slice) >= 3:
    print(word[start_index:start_index + 3])

