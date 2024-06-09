
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n
    # Iterate through the list of work times
    for i in range(n):
        # Calculate the total time available for work and reading
        total_time = a[i] + t
        # Check if the total time available is greater than the number of days
        if total_time > n:
            # If it is, calculate the minimum number of days needed to finish reading
            min_days = min(min_days, total_time // n)
    # Return the minimum number of days
    return min_days

