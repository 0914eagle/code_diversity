
def get_students_not_passed(A, B, C, N):
    if A + B + C != N:
        return -1
    if A + B < C or B + C < A or A + C < B:
        return -1
    return N - A - B - C

def main():
    A, B, C, N = map(int, input().split())
    print(get_students_not_passed(A, B, C, N))

if __name__ == '__main__':
    main()

