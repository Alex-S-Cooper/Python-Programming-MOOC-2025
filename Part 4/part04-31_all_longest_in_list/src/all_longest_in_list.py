# Write your solution here
def all_the_longest(list):
    longest_list = []
    length = 0
    for word in list:
        if len(word) > length:
            length = len(word)
    for word in list:
        if len(word) == length:
            longest_list.append(word)
    return longest_list