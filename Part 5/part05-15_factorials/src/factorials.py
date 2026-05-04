# Write your solution here
def factorials(n: int):
    factorials_dict = {}
    for i in range(n):
        sum = 1
        for j in range(i + 1, 0, -1):
            sum *= j
        factorials_dict[i + 1] = sum
    return factorials_dict