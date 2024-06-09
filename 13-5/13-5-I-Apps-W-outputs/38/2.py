
def get_failed_students(a, b, c, n):
    if a + b + c != n:
        return -1
    if a < 0 or b < 0 or c < 0 or n < 0:
        return -1
    if a == 0 and b == 0 and c == 0:
        return n
    if a == 0 and b == 0 and c > 0:
        return n - 1
    if a == 0 and b > 0 and c == 0:
        return n - 1
    if a > 0 and b == 0 and c == 0:
        return n - 1
    if a == n:
        return 0
    if b == n:
        return 0
    if c == n:
        return 0
    if a + b == n:
        return 1
    if a + c == n:
        return 1
    if b + c == n:
        return 1
    return -1

if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    failed_students = get_failed_students(a, b, c, n)
    print(failed_students)

