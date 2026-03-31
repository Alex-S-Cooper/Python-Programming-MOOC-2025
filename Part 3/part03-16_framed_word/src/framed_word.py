word = input("Word: ")
i = 1
start_space = " " * ((28 - len(word)) // 2)
end_space = start_space + (" " * (len(word) % 2))
while i <= 3:
    if i == 2:
        print("*" + start_space + word + end_space + "*")
    else:
        print("*" * 30)
    i += 1
