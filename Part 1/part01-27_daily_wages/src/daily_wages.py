hourly_wage = float(input("Hourly wage:"))
hours_worked = int(input("Hours worked:"))
day = input(("Day of the week:"))
daily_wage = hourly_wage * hours_worked
if day == "Sunday":
    daily_wage = daily_wage * 2
print(f"Daily wages: {daily_wage} euros")