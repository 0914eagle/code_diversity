
def solve(n, t, a):
    # Initialize variables
    days = 0
    total_time = 0

    # Iterate through the list of work times
    for i in range(n):
        # Check if there is enough time to read the book on this day
        if total_time + a[i] <= t:
            # Add the work time to the total time
            total_time += a[i]
        else:
            # Increment the number of days
            days += 1
            # Reset the total time
            total_time = a[i]

    # Return the minimum number of days
    return days

