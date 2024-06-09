
def solve(n, days):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1

    # Iterate through the days
    for i in range(n):
        # Check if the gym is open and the contest is carried out
        if days[i] in [2, 3]:
            # Check if the last day was a sport day
            if last_day_sport == i-1:
                # If it was, increase the rest days by 1
                rest_days += 1
            # Update the last day sport and contest days
            last_day_sport = i
            last_day_contest = i

    # Return the minimum number of rest days
    return rest_days

