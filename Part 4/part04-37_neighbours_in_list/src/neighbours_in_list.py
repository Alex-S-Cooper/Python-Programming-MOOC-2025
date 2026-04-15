# Write your solution here
def longest_series_of_neighbours(list):
    longest_series = 1
    series = 1
    for i in range(len(list)):
        if i != 0:
            if list[i] == list[i-1] + 1 or list[i] == list[i-1] - 1:
                series += 1
            else:
                series = 1
            if series > longest_series:
                longest_series = series
        print(f"i is {i}")
        print(f"series is {series}")
        print(f"longest series is {longest_series}")
    return longest_series

