# Write your solution here
def distinct_numbers(num_list):
    new_list = []
    for num in num_list:
        if num in new_list:
            continue
        new_list.append(num)
    return sorted(new_list)