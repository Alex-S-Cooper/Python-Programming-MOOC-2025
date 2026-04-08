# Write your solution here
items = int(input("How many items: "))
list = []
i = 1
while i <= items:
    item = int(input(f"Item {i}: "))
    list.append(item)
    i += 1
print(list)