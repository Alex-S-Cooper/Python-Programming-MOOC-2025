# write your solution here
def largest():
    with open("numbers.txt") as numbers_file:
        numbers = [int(num) for num in numbers_file]
        return max(numbers)

