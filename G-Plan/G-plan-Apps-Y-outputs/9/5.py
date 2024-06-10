
def min_days_to_finish_coursework(n, m, caffeine_levels):
    caffeine_levels.sort(reverse=True)
    pages_written = 0
    days = 0

    while pages_written < m:
        for caffeine in caffeine_levels:
            pages_written += max(0, caffeine - days)
            if pages_written >= m:
                return days + 1
        days += 1

    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    caffeine_levels = list(map(int, input().split()))
    result = min_days_to_finish_coursework(n, m, caffeine_levels)
    print(result)
