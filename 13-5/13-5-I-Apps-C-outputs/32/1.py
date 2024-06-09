
def get_students_and_bugs(n, m, s, a, b, c):
    students = []
    bugs = []
    for i in range(n):
        students.append([i, b[i], c[i]])
    for j in range(m):
        bugs.append([j, a[j]])
    return students, bugs

def get_optimal_schedule(students, bugs, s):
    schedule = []
    for i in range(len(students)):
        student = students[i]
        for j in range(len(bugs)):
            bug = bugs[j]
            if student[1] >= bug[1] and student[2] > 0:
                schedule.append([student[0], bug[0]])
                student[2] -= 1
                bug[1] = 0
    return schedule

def get_passes_needed(schedule, students):
    passes_needed = 0
    for i in range(len(schedule)):
        student = students[schedule[i][0]]
        passes_needed += student[2]
    return passes_needed

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    students, bugs = get_students_and_bugs(n, m, s, a, b, c)
    schedule = get_optimal_schedule(students, bugs, s)
    passes_needed = get_passes_needed(schedule, students)
    if passes_needed > s:
        print("NO")
    else:
        print("YES")
        for i in range(len(schedule)):
            print(schedule[i][0], end=" ")

if __name__ == '__main__':
    main()

