
from collections import namedtuple

def get_student_info():
    num_students = int(input())
    column_names = input().split()
    Student = namedtuple('Student', column_names)
    students = []
    for _ in range(num_students):
        student_info = input().split()
        students.append(Student(*student_info))
    return students

def calculate_average(students):
    total_marks = 0
    for student in students:
        total_marks += int(student.MARKS)
    return total_marks / len(students)

def main():
    students = get_student_info()
    average = calculate_average(students)
    print(f"{average:.2f}")

if __name__ == '__main__':
    main()

