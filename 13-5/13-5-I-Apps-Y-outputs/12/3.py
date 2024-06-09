
import collections
import statistics

def get_student_info(n):
    student_info = []
    for _ in range(n):
        student_info.append(input().split())
    return student_info

def get_average_marks(student_info):
    marks = []
    for student in student_info:
        marks.append(int(student[1]))
    return statistics.mean(marks)

def main():
    n = int(input())
    student_info = get_student_info(n)
    average_marks = get_average_marks(student_info)
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    main()

