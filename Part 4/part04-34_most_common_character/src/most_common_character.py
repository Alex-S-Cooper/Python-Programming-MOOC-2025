# Write your solution here
def most_common_character(string):
    most_common = ""
    most_common_count = 0
    for letter in string:
        if string.count(letter) > most_common_count:
            most_common = letter
            most_common_count = string.count(letter)
    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))