# Write your solution here
def shortest(word_list):
    shortest = word_list[0]
    for word in word_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest