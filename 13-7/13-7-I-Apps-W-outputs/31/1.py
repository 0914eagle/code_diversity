
def solve(n, t, a):
    # Initialize the minimum number of days to finish reading the book as n
    min_days = n
    
    # Iterate over each day
    for i in range(n):
        # Calculate the total time spent on work and reading for the current day
        total_time = a[i] + t
        
        # If the total time is less than or equal to 86400 (the number of seconds in a day), update the minimum number of days to finish reading the book
        if total_time <= 86400:
            min_days = min(min_days, i + 1)
    
    return min_days

