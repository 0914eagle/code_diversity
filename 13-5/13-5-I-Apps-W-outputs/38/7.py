
def get_failed_students(A, B, C, N):
    if A + B + C != N:
        return -1
    if A < 0 or B < 0 or C < 0 or N < 0:
        return -1
    if A + B < C or B + C < A or A + C < B:
        return -1
    return N - A - B - C

def main():
    A, B, C, N = map(int, input().split())
    print(get_failed_students(A, B, C, N))

if __name__ == '__main__':
    main()

