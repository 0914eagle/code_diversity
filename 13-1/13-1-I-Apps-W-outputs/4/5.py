
def get_max_days(n, m, a):
    # Initialize the variables
    b = [0] * n
    count = 0
    days = 0
    
    # Loop through each participant
    for i in range(n):
        # Loop through each food package
        for j in range(m):
            # If the food package is not already assigned to another participant
            if b[j] == 0:
                # Assign the food package to the current participant
                b[j] = i + 1
                count += 1
                # If all food packages are assigned, break the loop
                if count == m:
                    break
        # If all participants have been assigned a food package, break the loop
        if count == m:
            break
    
    # Loop through each participant and check if they have the same food type
    for i in range(n):
        for j in range(i + 1, n):
            # If the food types are not the same, break the loop
            if b[i] != b[j]:
                return days
        # If all participants have the same food type, increment the number of days
        days += 1
    
    # Return the number of days
    return days

