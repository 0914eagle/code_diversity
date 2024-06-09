
def get_max_days(n, m, a):
    # Initialize the variables
    b = [0] * n
    count = 0
    days = 0
    
    # Loop through each participant
    for i in range(n):
        # If the current participant has not been assigned a food type, assign one
        if b[i] == 0:
            b[i] = a[count]
            count += 1
        
        # If all food types have been assigned, break the loop
        if count == m:
            break
    
    # Loop through each food type
    for j in range(1, max(a) + 1):
        # If the current food type has been assigned to at least one participant, increment the day count
        if j in b:
            days += 1
    
    # Return the maximum number of days the expedition can last
    return days

