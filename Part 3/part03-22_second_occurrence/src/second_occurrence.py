word = input("Please type in a word: ")
substring = input("Please type in a character: ")
first_occurrence_start = word.find(substring)
first_occurrence_end = first_occurrence_start + len(substring)
new_word = word[first_occurrence_end: ]
if substring in new_word:
    second_index = first_occurrence_end + new_word.find(substring)
    print(f"The second occurrence of the substring is at index {second_index}.")
else:
    print("The substring does not occur twice in the string.")