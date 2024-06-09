
def solve(n, d, opponents):
    max_consecutive_days = 0
    current_consecutive_days = 0
    for i in range(d):
        present_opponents = 0
        for j in range(n):
            if opponents[i][j] == "1":
                present_opponents += 1
        if present_opponents == 0:
            current_consecutive_days += 1
        else:
            max_consecutive_days = max(max_consecutive_days, current_consecutive_days)
            current_consecutive_days = 0
    return max(max_consecutive_days, current_consecutive_days)

