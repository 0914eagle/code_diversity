
def solve(n, t, a):
    # Initialize a variable to store the minimum number of days
    min_days = n
    # Iterate through the list of work times
    for i in range(n):
        # Check if the total time spent on work is greater than the time required to read the book
        if sum(a[:i]) > t:
            # If it is, return the current day as the minimum
            return i
        # If the total time spent on work is less than the time required to read the book, continue to the next day
    # If the loop completes and no day is found, return the initial minimum of n days
    return min_days

