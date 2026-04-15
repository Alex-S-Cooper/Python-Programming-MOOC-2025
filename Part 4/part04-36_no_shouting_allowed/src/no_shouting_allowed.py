# Write your solution here
def no_shouting(list):
    new_list = []
    for i in list:
        if not i.isupper():
            new_list.append(i)
    return new_list
