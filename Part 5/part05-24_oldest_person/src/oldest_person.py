# Write your solution here
def oldest_person(people: list):
    return min(people, key=lambda x: x[1])[0]