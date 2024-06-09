
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n
    # Iterate over the days
    for i in range(n):
        # Calculate the total time available for work and reading
        total_time = a[i] + t
        # Check if the total time is greater than the number of seconds in a day
        if total_time > 86400:
            # If it is, calculate the number of days required to finish reading
            days = total_time // 86400
            # Update the minimum number of days if necessary
            min_days = min(min_days, days)
    # Return the minimum number of days
    return min_days

