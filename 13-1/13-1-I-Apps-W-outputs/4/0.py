
def get_max_days(n, m, a):
    # Initialize the variables
    b = [0] * n
    count = 0
    days = 0
    
    # Loop through each participant
    for i in range(n):
        # Loop through each food package
        for j in range(m):
            # If the current food package is not already assigned to another participant
            if b[j] == 0:
                # Assign the current food package to the current participant
                b[j] = i + 1
                count += 1
                # If all food packages are assigned, break the loop
                if count == m:
                    break
        # If all participants have been assigned a food package, break the loop
        if count == m:
            break
    
    # Loop through each participant
    for i in range(n):
        # Loop through each food package
        for j in range(m):
            # If the current food package is assigned to the current participant
            if b[j] == i + 1:
                # Increment the number of days by 1
                days += 1
    
    # Return the maximum number of days
    return days

