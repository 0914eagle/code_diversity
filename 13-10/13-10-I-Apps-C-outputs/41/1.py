
def get_students(n, m, s, a, b, c):
    students = [(i, b[i-1], c[i-1]) for i in range(1, n+1)]
    students.sort(key=lambda x: x[1], reverse=True)
    bugs = [(j, a[j-1]) for j in range(1, m+1)]
    bugs.sort(key=lambda x: x[1])
    days = 0
    passes = 0
    result = []
    for student in students:
        for bug in bugs:
            if student[1] >= bug[1] and passes + student[2] <= s:
                result.append(student[0])
                days += 1
                passes += student[2]
                break
        else:
            continue
        break
    if passes > s:
        return "NO"
    return "YES\n" + " ".join(map(str, result))

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_students(n, m, s, a, b, c))

if __name__ == '__main__':
    main()

