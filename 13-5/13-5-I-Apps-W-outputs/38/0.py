
def get_students_who_didnt_pass(a, b, c, n):
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
        return n - 3 * a
    if a == b and b != c and a > 0 and b > 0 and c > 0:
        return n - 2 * a - b
    if a != b and b == c and a > 0 and b > 0 and c > 0:
        return n - a - 2 * b
    if a != b and b != c and a > 0 and b > 0 and c > 0:
        return n - a - b - c
    return -1

if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    result = get_students_who_didnt_pass(a, b, c, n)
    print(result)

