
def solve(k, a):
    # Initialize variables
    days = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(a)):
        days[i] = a[i]
    days_visited = 0
    current_day = 0
    min_days = k
    while days_visited < k:
        # If there are classes on the current day, visit the day
        if days[current_day]:
            days_visited += 1
        # If we have visited all the days, start again from the beginning
        if current_day == 6:
            current_day = 0
        else:
            current_day += 1
        # If we have visited more than the minimum number of days, break
        if days_visited > min_days:
            break
    return min_days

