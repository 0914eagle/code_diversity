
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n + 1
    
    # Iterate over each day
    for i in range(n):
        # Calculate the total time spent on work and reading for the current day
        total_time = a[i] + t
        
        # If the total time is less than or equal to the number of seconds in a day, we can finish reading the book on the current day
        if total_time <= 86400:
            min_days = min(min_days, i + 1)
    
    return min_days

