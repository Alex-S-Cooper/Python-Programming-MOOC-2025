number = int(input("Please type in a number: "))

pair_count = 0
i = 0
pos_neg = 0
while i < number:
    if pos_neg == 0:
        print(pair_count + 1)
        pos_neg = 1
        i += 1
        continue
    elif pos_neg == 1:
        print(number - pair_count)
        pos_neg = 0
        i += 1
    pair_count += 1
    
   

