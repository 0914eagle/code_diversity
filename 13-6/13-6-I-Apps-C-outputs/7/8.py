
import sys
input = sys.stdin.read()
n, k = map(int, input.split('\n')[0].split())
courses = [tuple(input.split('\n')[i].split()) for i in range(1, n+1)]

def f1(courses, k):
    courses.sort(key=lambda x: x[1])
    return sum([c[1] for c in courses[:k]])

def f2(courses, k):
    courses.sort(key=lambda x: x[1])
    total = 0
    for i in range(k):
        total += courses[i][1]
        if courses[i][0].endswith('1'):
            for j in range(i+1, k):
                if courses[j][0] == courses[i][0][:-1] + '2':
                    total += courses[j][1]
                    break
    return total

if __name__ == '__main__':
    print(f1(courses, k))
    print(f2(courses, k))

