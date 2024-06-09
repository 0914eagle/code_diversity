
def solve(n, t, a):
    # Initialize a counter for the number of days spent reading
    days_spent_reading = 0
    
    # Iterate through each day
    for i in range(n):
        # Check if there is enough time to read on this day
        if t - a[i] >= 0:
            # Subtract the time spent working from the total time required to read the book
            t = t - a[i]
            # Increment the number of days spent reading
            days_spent_reading += 1
        else:
            # If there is not enough time to read on this day, break the loop
            break
    
    # Return the minimum number of days spent reading
    return days_spent_reading

