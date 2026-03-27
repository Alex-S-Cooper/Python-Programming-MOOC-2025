story = ""
old_word = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == old_word:
        break
    story += word + " "
    old_word = word
print(story)