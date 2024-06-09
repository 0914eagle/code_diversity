
def get_days_needed(m, n, a):
    days = 0
    pages_written = 0
    for i in range(n):
        pages_written += max(0, a[i] - days)
        days += 1
        if pages_written >= m:
            return days
    return -1

