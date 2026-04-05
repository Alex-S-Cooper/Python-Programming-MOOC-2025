# Write your solution here
def squared(string, length):
    i = 0
    new_string = string
    while len(new_string) <= length * length:
        new_string *= 2
    while i < length:
        print(new_string[0:length])
        new_string = new_string[length:]
        i += 1
# Testing the function
if __name__ == "__main__":
    squared("ab", 3)

