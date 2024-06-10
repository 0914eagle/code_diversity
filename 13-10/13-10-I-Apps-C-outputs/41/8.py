
import sys
import itertools

def get_input():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n, m, s, a, b, c

def get_passes(c):
    return sum(c)

def get_days(b, a):
    return [b_i // a_i for b_i, a_i in zip(b, a)]

def get_optimal_solution(n, m, s, a, b, c):
    days = get_days(b, a)
    passes = get_passes(c)
    if passes > s:
        return "NO"
    
    students = list(range(1, n+1))
    bug_to_student = {}
    for i in range(m):
        student = min(students, key=lambda x: days[x-1])
        bug_to_student[i+1] = student
        students.remove(student)
    
    return "YES\n" + " ".join(str(bug_to_student[i]) for i in range(1, m+1))

def main():
    n, m, s, a, b, c = get_input()
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()

