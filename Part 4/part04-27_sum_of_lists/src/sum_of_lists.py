# Write your solution here
def list_sum(list1, list2):
    new_list = []
    for num1, num2 in zip(list1, list2):
        new_list.append(num1 + num2)
    return new_list