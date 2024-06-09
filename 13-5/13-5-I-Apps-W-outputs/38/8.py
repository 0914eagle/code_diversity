
def get_students_not_passed(a, b, c, n):
    if a + b + c != n:
        return -1
    if a < 0 or b < 0 or c < 0 or n < 0:
        return -1
    if a == 0 and b == 0 and c == 0:
        return n
    if a == 0 and b == 0 and c > 0:
        return n - c
    if a == 0 and b > 0 and c == 0:
        return n - b
    if a > 0 and b == 0 and c == 0:
        return n - a
    if a == b and b == c and a > 0:
        return n - a
    if a == b and b != c and a > 0:
        return n - a
    if a != b and b == c and a > 0:
        return n - a
    return -1

if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    print(get_students_not_passed(a, b, c, n))

