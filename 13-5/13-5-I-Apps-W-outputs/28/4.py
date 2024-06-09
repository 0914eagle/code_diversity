
def solve(n, t, a):
    # Initialize variables
    day = 1
    time_spent = 0
    total_time = 0

    # Loop through the days
    while day <= n:
        # Check if there is enough time to read the book on this day
        if time_spent + t <= 86400:
            # Add the time spent on work to the total time
            total_time += time_spent
            # Break out of the loop
            break
        # Add the time spent on work to the total time
        total_time += time_spent
        # Subtract the time spent on work from the total time
        time_spent = 86400 - time_spent
        # Increment the day
        day += 1

    # Return the minimum day
    return day

