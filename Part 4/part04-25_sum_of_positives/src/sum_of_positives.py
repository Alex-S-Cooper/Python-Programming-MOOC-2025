# Write your solution here

def sum_of_positives(num_list):
    sum = 0
    for num in num_list:
        if num > 0:
            sum += num
    return sum
