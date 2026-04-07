# Copy here code of line function from previous exercise and use it in your solution
def line(length, char):
    if char == "":
        print("*" * length)
    else:
        char = char[0]
        print(char * length)

def shape(triangle_size, char1, square_size, char2):
    i = 1
    while i <= triangle_size:
        line(i, char1)
        i += 1
    j = 0
    while j < square_size:
        line(triangle_size, char2)
        j += 1
        


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")