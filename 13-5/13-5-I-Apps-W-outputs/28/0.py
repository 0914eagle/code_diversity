
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n
    
    # Iterate through the list of work times
    for i in range(n):
        # Calculate the total time available for work and reading
        total_time = a[i] + t
        
        # If the total time available is greater than the time required to read the book, update the minimum number of days
        if total_time >= t:
            min_days = min(min_days, i + 1)
    
    return min_days

