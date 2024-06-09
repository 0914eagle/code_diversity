
def solve(n, t, a):
    # Initialize the minimum number of days to finish reading the book as n
    min_days = n
    
    # Iterate over the work time for each day
    for i in range(n):
        # Calculate the total time available for work and reading on the current day
        total_time = a[i] + t
        
        # If the total time available is greater than or equal to the time required to read the book,
        # then the current day is a possible day to finish reading the book
        if total_time >= t:
            min_days = min(min_days, i + 1)
    
    return min_days

