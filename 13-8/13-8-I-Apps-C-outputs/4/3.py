
def solve(n, arr):
    # Count the number of days Vasya spends doing sport and writing the contest
    sport_days = sum(arr)
    contest_days = sum(arr)
    
    # Loop through the array and check if Vasya does sport and writes the contest on the same day
    for i in range(n):
        if arr[i] == 1 and arr[i-1] == 1:
            sport_days -= 1
        if arr[i] == 2 and arr[i-1] == 2:
            contest_days -= 1
    
    # Return the minimum number of days Vasya has a rest
    return min(sport_days, contest_days)

