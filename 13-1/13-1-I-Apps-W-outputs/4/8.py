
def get_max_days(n, m, a):
    # Initialize the variables
    b = [0] * n
    count = 0
    days = 0
    
    # Loop through each participant
    for i in range(n):
        # Check if the current participant has already eaten
        if b[i] == 0:
            # Assign a food type to the current participant
            b[i] = a[count]
            count += 1
        # Check if all food types have been assigned
        if count == m:
            count = 0
            days += 1
    
    # Return the maximum number of days the expedition can last
    return days

