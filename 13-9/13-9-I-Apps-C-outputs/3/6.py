
def solve(n, a):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1

    # Iterate through the days
    for i in range(n):
        # Check if the gym is open and a contest is carried out
        if a[i] in [2, 3]:
            # If the gym is open and a contest is carried out, increase the rest days
            rest_days += 1
            # Set the last day of sport and contest to the current day
            last_day_sport = i
            last_day_contest = i
        # Check if the gym is closed and a contest is carried out
        elif a[i] == 1:
            # If the gym is closed and a contest is carried out, increase the rest days
            rest_days += 1
            # Set the last day of contest to the current day
            last_day_contest = i
        # Check if the gym is open and no contest is carried out
        elif a[i] == 2:
            # If the gym is open and no contest is carried out, do sport on the current day
            last_day_sport = i

    # Check if the last day of sport and contest are not the same
    if last_day_sport != last_day_contest:
        # Increase the rest days by 1
        rest_days += 1

    return rest_days

