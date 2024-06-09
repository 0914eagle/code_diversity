
def get_marks(marks):
    return sum(marks) / len(marks)

def get_average_marks(marks_list):
    return [get_marks(marks) for marks in marks_list]

def get_student_average(student_name, student_marks):
    return get_average_marks(student_marks[student_name])

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(int, line))
        student_marks[name] = scores
    query_name = input()
    print(f"{query_name}'s average score is {get_student_average(query_name, student_marks):.2f}")

if __name__ == '__main__':
    main()

