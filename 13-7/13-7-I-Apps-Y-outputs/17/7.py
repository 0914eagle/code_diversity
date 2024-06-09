
def solve(a):
    N = len(a)
    if N < 2:
        return "Yes"
    if N % 2 == 1:
        return "No"
    for i in range(N // 2):
        if a[i] * a[N - 1 - i] % 4 != 0:
            return "No"
    return "Yes"

