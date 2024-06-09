
def f1(A, B, C, N):
    if A + B + C != N:
        return -1
    if A < 0 or B < 0 or C < 0 or N < 0:
        return -1
    if A == 0 and B == 0 and C == 0:
        return -1
    if A != 0 and B != 0 and C != 0:
        return N - A - B - C
    return -1

def f2(A, B, C, N):
    if A + B + C != N:
        return -1
    if A < 0 or B < 0 or C < 0 or N < 0:
        return -1
    if A == 0 and B == 0 and C == 0:
        return -1
    if A != 0 and B != 0 and C != 0:
        return N - A - B - C
    return -1

if __name__ == '__main__':
    A, B, C, N = map(int, input().split())
    print(f1(A, B, C, N))
    print(f2(A, B, C, N))

