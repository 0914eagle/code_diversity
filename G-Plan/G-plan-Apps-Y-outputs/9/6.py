
def min_days_to_finish_coursework(n, m, coffee_cups):
    coffee_cups.sort(reverse=True)
    pages_written = 0
    days = 0

    while pages_written < m:
        day_pages = 0
        for caffeine in coffee_cups:
            if caffeine > 0:
                day_pages += max(0, caffeine - days)
                caffeine -= 1
            if day_pages >= m - pages_written:
                break
        if day_pages == 0:
            return -1
        pages_written += day_pages
        days += 1

    return days

if __name__ == "__main__":
    n, m = map(int, input().split())
    coffee_cups = list(map(int, input().split()))
    print(min_days_to_finish_coursework(n, m, coffee_cups))
