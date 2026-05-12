# Write your solution here
def add_student(students, name):
    students[name] = []

def create_average_grade(students, name):
    sum = 0
    for course in students[name]:
        sum += course[1]
    average_grade = sum / len(students[name])
    return average_grade 

def print_student(students, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    elif not students[name]:
        print(f"{name}:")
        print(f" no completed courses")
    else:
        print(f"{name}:")
        if len(students[name]) == 1:
            course = students[name][0]
            print(f" 1 completed courses:")  # Had to change from "course" to pass the test
            print(f"  {course[0]} {course[1]}")
        else:
            print(f" {len(students[name])} completed courses:")
            for course in students[name]:
                print(f"  {course[0]} {course[1]}")
        print(f" average grade {create_average_grade(students, name)}")

def add_course(students, name, new_course):
    course_list = students[name]
    for course in course_list:
        if new_course[0] == course[0]:
            if new_course[1] > course[1]:
                course_list.remove(course)
                course_list.append(new_course)
            return
    if new_course[1] > 0:
        course_list.append(new_course)

def create_student_summary(students):
    students_summary = {}
    for student, courses in students.items():
        course_count = len(courses)
        average_grade = create_average_grade(students, student)
        students_summary[student] = (course_count, average_grade)
    return students_summary

def most_courses_completed(students_summary):
    most_courses_key = ""
    most_courses_value = 0
    for name, course in students_summary.items():
        if course[0] > most_courses_value:
            most_courses_value = course[0]
            most_courses_key = name
    return most_courses_key, most_courses_value

def highest_average(students_summary):
    highest_average_key = ""
    highest_average_value = 0
    for name, course in students_summary.items():
        if course[1] > highest_average_value:
            highest_average_value = course[1]
            highest_average_key = name
    return highest_average_key, highest_average_value

def summary(students):
    students_summary = create_student_summary(students)
    most_courses_name, most_courses_value = most_courses_completed(students_summary)
    highest_average_name, highest_average_value = highest_average(students_summary)

    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_value} {most_courses_name}")
    print(f"best average grade {highest_average_value} {highest_average_name}")

def main():
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 5))
    summary(students)

if __name__ == "__main__":
    main()