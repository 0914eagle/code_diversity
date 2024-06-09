
from collections import namedtuple

def get_student_data(n):
    columns = input().split()
    Student = namedtuple('Student', columns)
    students = []
    for _ in range(n):
        students.append(Student(*input().split()))
    return students

def get_average_marks(students):
    marks = [student.MARKS for student in students]
    return sum(marks) / len(marks)

def main():
    n = int(input())
    students = get_student_data(n)
    average_marks = get_average_marks(students)
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    main()

