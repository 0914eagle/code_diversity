
def get_marks_average(marks):
    return sum(marks) / len(marks)

def get_student_average(student_marks):
    return get_marks_average(student_marks)

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(int, marks))
    query_name = input()
    print(f"{get_student_average(student_marks[query_name]):.2f}")

if __name__ == '__main__':
    main()

