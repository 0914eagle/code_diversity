
def get_students_to_fix_bugs(n, m, s, bugs, students):
    students = sorted(students, reverse=True)
    bugs = sorted(bugs)
    students_to_fix_bugs = []
    days = 0
    for i in range(n):
        student = students[i]
        for j in range(m):
            bug = bugs[j]
            if student >= bug:
                students_to_fix_bugs.append(i+1)
                days += 1
                break
    if days > s:
        return "NO"
    return "YES\n" + " ".join(map(str, students_to_fix_bugs))

def main():
    n, m, s = map(int, input().split())
    bugs = list(map(int, input().split()))
    students = list(map(int, input().split()))
    print(get_students_to_fix_bugs(n, m, s, bugs, students))

if __name__ == '__main__':
    main()

