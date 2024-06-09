
def solve(n, arr):
    # Initialize variables to keep track of the number of days Vasya rests and the number of consecutive days he spends doing sport or writing contests
    rest_days = 0
    consecutive_sport_days = 0
    consecutive_contest_days = 0
    
    # Iterate through the array of information about each day
    for i in range(n):
        # If the gym is closed and the contest is not carried out, Vasya rests
        if arr[i] == 0:
            rest_days += 1
        # If the gym is closed and the contest is carried out, Vasya writes the contest and rests
        elif arr[i] == 1:
            rest_days += 1
            consecutive_contest_days += 1
        # If the gym is open and the contest is not carried out, Vasya does sport
        elif arr[i] == 2:
            consecutive_sport_days += 1
        # If the gym is open and the contest is carried out, Vasya does sport and writes the contest
        elif arr[i] == 3:
            consecutive_sport_days += 1
            consecutive_contest_days += 1
    
    # If Vasya does sport on two consecutive days, he must rest on the third day
    if consecutive_sport_days > 1:
        rest_days += 1
    
    # If Vasya writes the contest on two consecutive days, he must rest on the third day
    if consecutive_contest_days > 1:
        rest_days += 1
    
    return rest_days

