times_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
student_meal = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
weekly_spend = groceries + times_per_week * student_meal
daily_spend = weekly_spend / 7

print(f"Average food expenditure:")
print(f"Daily: {daily_spend} euros")
print(f"Weekly: {weekly_spend} euros")