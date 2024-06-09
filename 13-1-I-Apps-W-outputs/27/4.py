
def solve(A, B, C, N):
    if A + B + C != N:
        return -1
    if A + B < C or B + C < A or C + A < B:
        return -1
    return N - A - B - C

