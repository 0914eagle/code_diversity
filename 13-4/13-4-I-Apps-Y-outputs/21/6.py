
def solve(m, n, t):
    time_complexity = [0, 1, 4, 9, 16, 25, 243, 1000000]
    if time_complexity[t] * n <= m:
        return "AC"
    else:
        return "TLE"

