# Write your solution here
def line(length, char):
    if char == "":
        print("*" * length)
    else:
        char = char[0]
        print(char * length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")