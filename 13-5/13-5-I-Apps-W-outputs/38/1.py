
def get_students_who_did_not_pass(a, b, c, n):
    if a + b + c != n:
        return -1
    if a + b < c or b + c < a or a + c < b:
        return -1
    return n - a - b - c

def main():
    a, b, c, n = map(int, input().split())
    print(get_students_who_did_not_pass(a, b, c, n))

if __name__ == '__main__':
    main()

