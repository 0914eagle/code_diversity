
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1

    # Iterate through the array
    for i in range(n):
        # Check if the gym is open and the contest is carried out
        if arr[i] == 3:
            # If the last day Vasya did sport, he needs a rest
            if last_day_sport == i-1:
                rest_days += 1
            # Update the last day Vasya did sport
            last_day_sport = i

        # Check if the contest is carried out and the gym is closed
        elif arr[i] == 1:
            # If the last day Vasya wrote the contest, he needs a rest
            if last_day_contest == i-1:
                rest_days += 1
            # Update the last day Vasya wrote the contest
            last_day_contest = i

    # Return the minimum number of rest days
    return rest_days

