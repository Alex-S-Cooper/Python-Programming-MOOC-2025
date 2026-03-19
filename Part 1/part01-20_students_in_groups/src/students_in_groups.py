students = int(input("How many students on the course? "))
group = int(input("Desired group size? "))
floor = students // group
remainder = students % group
groups = (students + group - 1) // group
print("Number of groups formed:", groups)