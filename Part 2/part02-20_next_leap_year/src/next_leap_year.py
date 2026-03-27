year = int(input("Year: "))
next_year = year

while True:
    next_year += 1
    if (next_year % 4 == 0 and next_year % 400 == 0) or (next_year % 4 == 0 and next_year % 100 != 0):
        break



print(f"The next leap year after {year} is {next_year}")