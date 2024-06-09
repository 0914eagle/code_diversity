
def solve(n, t, a):
    # Initialize the minimum number of days to finish reading the book as n
    min_days = n
    # Iterate through each day
    for i in range(n):
        # Calculate the total time spent on work and reading for the current day
        total_time = a[i] + t
        # If the total time is less than or equal to the number of seconds in a day, we can finish reading the book on the current day
        if total_time <= 86400:
            # Update the minimum number of days to finish reading the book if necessary
            min_days = min(min_days, i+1)
    # Return the minimum number of days to finish reading the book
    return min_days

