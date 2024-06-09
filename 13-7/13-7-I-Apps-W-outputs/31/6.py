
def solve(n, t, a):
    # Initialize the minimum number of days to finish reading the book as n
    min_days = n
    # Iterate over the work time for each day
    for i in range(n):
        # If the work time for the current day is greater than the time required to read the book,
        # then the minimum number of days to finish reading the book is the current day
        if a[i] > t:
            min_days = i
            break
    return min_days

