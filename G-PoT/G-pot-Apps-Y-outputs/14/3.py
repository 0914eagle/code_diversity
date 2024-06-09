
n = int(input())
student_marks = {}
for _ in range(n):
    name, *marks = input().split()
    student_marks[name] = list(map(int, marks))

query_name = input()

average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
print("{:.2f}".format(average_marks))
