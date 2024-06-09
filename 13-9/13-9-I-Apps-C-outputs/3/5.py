
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1
    
    # Iterate through the array
    for i in range(n):
        # Check if the gym is open and a contest is carried out
        if arr[i] in [2, 3]:
            # Check if the last day Vasya did sport was the previous day
            if last_day_sport == i-1:
                # Increment the number of rest days
                rest_days += 1
            # Update the last day Vasya did sport
            last_day_sport = i
        # Check if a contest is carried out and the gym is closed
        elif arr[i] == 1:
            # Check if the last day Vasya wrote the contest was the previous day
            if last_day_contest == i-1:
                # Increment the number of rest days
                rest_days += 1
            # Update the last day Vasya wrote the contest
            last_day_contest = i
    
    # Return the number of rest days
    return rest_days

