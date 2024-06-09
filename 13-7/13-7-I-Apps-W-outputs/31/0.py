
def solve(n, t, a):
    days = 0
    total_time = 0
    for i in range(n):
        total_time += a[i]
        if total_time >= t:
            return days + 1
        days += 1
    return days + 1

