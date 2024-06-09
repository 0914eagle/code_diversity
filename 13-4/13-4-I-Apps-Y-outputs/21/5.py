
def solve(m, n, t):
    complexity = [0, 1, 2, 4, 3, 5, 6, 7]
    if complexity[t] * n <= m:
        return "AC"
    else:
        return "TLE"

