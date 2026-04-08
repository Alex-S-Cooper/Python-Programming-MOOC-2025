# Write your solution here
def same_chars(word, i1, i2):
    if i1 > i2 or i2 >= len(word):
        return False
    elif word[i1] == word[i2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))