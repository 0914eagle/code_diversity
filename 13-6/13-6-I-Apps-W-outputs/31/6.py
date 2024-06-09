
def solve(k, a):
    # Initialize variables
    day = 1
    count = 0
    total_days = 0
    classes = 0

    # Iterate through the input array
    for i in range(len(a)):
        # If classes are held on the current day, increment the count
        if a[i] == 1:
            count += 1
        # If the count is equal to the required number of classes, increment the total days
        if count == k:
            total_days += 1
            count = 0
        # If the current day is Saturday, increment the total days
        if day == 7:
            total_days += 1
        # Increment the day
        day += 1
        # If the day is greater than 7, set it back to 1
        if day > 7:
            day = 1

    # Return the total days
    return total_days

