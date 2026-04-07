# Write your solution here
def spruce(size):
    side = size - 1
    length = size + side
    stars = 1
    i = 0
    print("a spruce!")
    while i <= size:
        if i == size:
            print(f"{side * " "}{"*"}{side * " "}")
        else:
            print(f"{(side - i) * " "}{(stars) * "*"}{(side - i) * " "}")
            stars += 2
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)