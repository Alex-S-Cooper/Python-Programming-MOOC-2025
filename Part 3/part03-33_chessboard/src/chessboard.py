# Write your solution here
def chessboard(length):
    c = 0
    num = 1
    while c < length:
        row = ""
        r = 0
        while r < length:
            row += str(num)
            if num == 0:
                num = 1
            elif num == 1:
                num = 0
            r += 1
        print(row)

        if row[0] == "0":
            num = 1
        elif row[0] == "1":
            num = 0

        c += 1
            
# Testing the function
if __name__ == "__main__":
    chessboard(3)
