# Write your solution here
def generate_exercise_points(exercises):
    exercise_points = []
    for exercise in exercises:
        exercise_points.append(exercise // 10)
    return exercise_points

def generate_exercise_and_exam_points(exam_points, exercise_points):
    exercise_and_exam_points = []
    for exam_point, exercise_point in zip(exam_points, exercise_points):
        exercise_and_exam_points.append(exam_point + exercise_point)
    return exercise_and_exam_points

def generate_grades(combined_points, exam_points):
    grades = []
    for i in range(len(combined_points)):
        if exam_points[i] < 10:
            grades.append(0)
        elif combined_points[i] > 0 and combined_points[i] <= 14:
            grades.append(0)
        elif combined_points[i] > 14  and combined_points[i] <= 17:
            grades.append(1)
        elif combined_points[i] > 17 and combined_points[i] <= 20:
            grades.append(2)
        if combined_points[i] > 20 and combined_points[i] <= 23:
            grades.append(3)
        if combined_points[i] > 23 and combined_points[i] <= 27:
            grades.append(4)
        if combined_points[i] > 27 and combined_points[i] <= 30:
            grades.append(5)  
    return grades

def print_statistics(points, grades):
    sum = 0
    passes = 0
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    for i in range(len(points)):
        sum += points[i]
        if grades[i] > 0:
            passes += 1
        if grades[i] == 0:
            grade0 += 1
        elif grades[i] == 1:
            grade1 += 1
        elif grades[i] == 2:
            grade2 += 1
        elif grades[i] == 3:
            grade3 += 1
        elif grades[i] == 4:
            grade4 += 1
        elif grades[i] == 5:
            grade5 += 1
    average = sum / len(points)
    pass_rate = (passes / len(grades)) * 100
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_rate:.1f}")
    print("Grade distribution:")
    print(f"  5: {"*" * grade5}")
    print(f"  4: {"*" * grade4}")
    print(f"  3: {"*" * grade3}")
    print(f"  2: {"*" * grade2}")
    print(f"  1: {"*" * grade1}")
    print(f"  0: {"*" * grade0}")
    

def main():
    exam_points = []
    exercises = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if not user_input:
            break
        data = user_input.split()
        exam_points.append(int(data[0]))
        exercises.append(int(data[1]))
        
    exercise_points = generate_exercise_points(exercises)
    combined_points = generate_exercise_and_exam_points(exam_points, exercise_points)
    grades = generate_grades(combined_points, exam_points)
    print_statistics(combined_points, grades)

main()

