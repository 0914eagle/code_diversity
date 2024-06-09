
def get_marks_average(marks):
    return sum(marks) / len(marks)

def get_student_marks(student_name, students):
    return students[student_name]

def get_average_marks(student_name, students):
    marks = get_student_marks(student_name, students)
    return get_marks_average(marks)

def main():
    students = {}
    for _ in range(int(input())):
        name = input()
        score = list(map(float, input().split()))
        students[name] = score
    query_name = input()
    average = get_average_marks(query_name, students)
    print(f"{average:.2f}")

if __name__ == '__main__':
    main()

