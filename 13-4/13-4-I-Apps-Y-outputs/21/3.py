
def solve(m, n, t):
    time_complexity = [0, 1, 2, 4, 9, 16, 25, 36]
    if time_complexity[t] * n <= m:
        return "AC"
    else:
        return "TLE"

