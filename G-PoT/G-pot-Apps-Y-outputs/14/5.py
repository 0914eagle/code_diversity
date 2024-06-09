
n = int(input())
student_marks = {}
for _ in range(n):
    name, *marks = input().split()
    marks = list(map(int, marks))
    student_marks[name] = marks

query_name = input()

if query_name in student_marks:
    avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(avg_marks))
