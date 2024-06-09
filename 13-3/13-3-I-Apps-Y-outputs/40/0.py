
def solve(p, n):
    # Initialize a list to store the number of days for each kid
    days = [0] * n
    # Loop through each day
    for day in range(1, n+1):
        # Loop through each kid
        for i in range(n):
            # If the current kid is the owner of the book
            if i == p[i]-1:
                # Set the number of days for the current kid to the current day
                days[i] = day
                # Break out of the loop
                break
    return days

