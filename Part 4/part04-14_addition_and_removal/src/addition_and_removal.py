# Write your solution here
list = []
while True:
    print(f"The list is now {list}")#
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "x":
        break
    elif command == "d":
        list.append(len(list) + 1)
    elif command == "r":
        list.remove(list[-1])
print("Bye!")