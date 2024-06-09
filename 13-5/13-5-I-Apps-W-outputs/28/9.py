
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n
    # Iterate through the list of free time for each day
    for i in range(n):
        # Check if the free time for the current day is greater than or equal to the time required to read the book
        if a[i] >= t:
            # If so, return the current day as the minimum number of days
            return i + 1
        # If the free time for the current day is less than the time required to read the book, update the minimum number of days
        min_days = min(min_days, i + 1 + (t - a[i]) // 86400)
    # Return the minimum number of days
    return min_days

