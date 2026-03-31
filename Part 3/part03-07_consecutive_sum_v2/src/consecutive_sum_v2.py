limit = int(input("Limit: "))
number = 1
sum = 1
sum_str = "1"
while sum < limit:
    number += 1
    sum += number
    sum_str += f" + {number}"
    
print(f"The consecutive sum: {sum_str} = {sum}")
