
def get_passes(students):
    total_passes = 0
    for student in students:
        total_passes += student[1]
    return total_passes

def get_bugs(bugs):
    return len(bugs)

def get_student_by_ability(students, ability):
    for student in students:
        if student[0] == ability:
            return student
    return None

def get_student_by_complexity(students, complexity):
    for student in students:
        if student[1] == complexity:
            return student
    return None

def get_optimal_solution(students, bugs):
    passes = get_passes(students)
    bugs_left = get_bugs(bugs)
    solution = []
    while bugs_left > 0 and passes > 0:
        for bug in bugs:
            student = get_student_by_ability(students, bug[0])
            if student:
                solution.append(student[2])
                passes -= 1
                bugs_left -= 1
                break
        for student in students:
            student[1] -= 1
    if bugs_left == 0 and passes == 0:
        return solution
    else:
        return None

def main():
    n, m, s = map(int, input().split())
    bugs = []
    for _ in range(m):
        bugs.append(list(map(int, input().split())))
    students = []
    for _ in range(n):
        students.append(list(map(int, input().split())))
    solution = get_optimal_solution(students, bugs)
    if solution:
        print("YES")
        print(*solution)
    else:
        print("NO")

if __name__ == '__main__':
    main()

