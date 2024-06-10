
def min_days_to_finish_coursework(n, m, coffee):
    coffee.sort(reverse=True)
    pages_written = 0
    days = 0

    while pages_written < m:
        for caffeine in coffee:
            pages_written += max(0, caffeine - days)
            if pages_written >= m:
                return days + 1
        days += 1

    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    coffee = list(map(int, input().split()))
    print(min_days_to_finish_coursework(n, m, coffee))
