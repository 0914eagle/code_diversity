
def find_min_days(n, k, a):
    total_candies = 0
    days = 0
    for i in range(n):
        total_candies += a[i]
        days += 1
        if total_candies >= k:
            return days
        if total_candies > k:
            return -1
    return -1

