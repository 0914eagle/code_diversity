
def get_marks_average(marks):
    return sum(marks) / len(marks)

def get_student_marks(student_name, students):
    return students[student_name]

def get_query_name(query_name, students):
    return query_name

def solve(students, query_name):
    student_marks = get_student_marks(query_name, students)
    average_marks = get_marks_average(student_marks)
    return average_marks

if __name__ == '__main__':
    n = int(input())
    students = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(int, line))
        students[name] = scores
    query_name = get_query_name(input(), students)
    average = solve(students, query_name)
    print(f"{average:.2f}")

