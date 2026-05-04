# Write your solution here
def dict_of_numbers():
    dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
            
    for i in range(20, 100, 10):
        stem = "twenty"
        if i == 30:
            stem = "thirty"
        elif i == 40:
            stem = "forty"
        elif i == 50:
            stem = "fifty"
        elif i == 60:
            stem = "sixty"
        elif i == 70:
            stem = "seventy"
        elif i == 80:
            stem = "eighty"
        elif i == 90:
            stem = "ninety" 
        for j in range(10):
            number = ""
            if j != 0:
                number = f"{stem}-{dict[j]}"
            else:
                number = stem
            dict[i + j] = number

    return dict