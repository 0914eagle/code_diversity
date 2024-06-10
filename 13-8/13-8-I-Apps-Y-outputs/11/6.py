
from collections import namedtuple

def read_data(N):
    columns = input().split()
    Student = namedtuple('Student', columns)
    students = []
    for _ in range(N):
        students.append(Student(*input().split()))
    return students

def get_average_marks(students):
    marks = [float(student.MARKS) for student in students]
    return sum(marks) / len(marks)

def main():
    N = int(input())
    students = read_data(N)
    average_marks = get_average_marks(students)
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    main()

