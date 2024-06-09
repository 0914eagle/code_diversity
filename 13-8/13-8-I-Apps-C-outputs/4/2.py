
def solve(n, arr):
    # Initialize variables to keep track of the number of consecutive days Vasya spends doing sport or writing contests
    consecutive_sport_days = 0
    consecutive_contest_days = 0
    # Initialize variable to keep track of the minimum number of days Vasya has a rest
    min_rest_days = 0
    
    # Iterate through the array of information about each day
    for i in range(n):
        # If the gym is open on this day
        if arr[i] % 2 == 1:
            # If Vasya does sport on this day, increment the number of consecutive sport days
            if arr[i] == 1 or arr[i] == 3:
                consecutive_sport_days += 1
            # If Vasya writes the contest on this day, increment the number of consecutive contest days
            if arr[i] == 2 or arr[i] == 3:
                consecutive_contest_days += 1
        # If the gym is closed on this day
        else:
            # If Vasya writes the contest on this day, increment the number of consecutive contest days
            if arr[i] == 1:
                consecutive_contest_days += 1
        
        # If Vasya has completed two consecutive days of doing sport or writing contests, increment the minimum number of days he has a rest
        if consecutive_sport_days == 2 or consecutive_contest_days == 2:
            min_rest_days += 1
            consecutive_sport_days = 0
            consecutive_contest_days = 0
    
    # Return the minimum number of days Vasya has a rest
    return min_rest_days

