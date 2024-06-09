
def solve(n, t, a):
    # Initialize the minimum number of days to finish reading the book as n
    min_days = n
    
    # Iterate through each day
    for i in range(n):
        # Calculate the total time available for work and reading on the current day
        total_time = a[i] + t
        
        # If the total time is greater than the number of seconds in a day, subtract the number of seconds in a day
        if total_time > 86400:
            total_time -= 86400
        
        # Update the minimum number of days to finish reading the book if the current day has the minimum number of days
        if total_time < min_days:
            min_days = total_time
    
    return min_days

