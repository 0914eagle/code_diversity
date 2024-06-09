
def get_max_days(n, k, a):
    # Initialize variables
    days = 0
    total_cut = 0
    
    # Loop through each bamboo
    for i in range(n):
        # Check if the bamboo has reached the required height
        if a[i] <= days:
            # Calculate the length of the cut part
            cut = days - a[i]
            
            # Check if the total length of cut parts is less than or equal to k
            if total_cut + cut <= k:
                # Increment the total length of cut parts
                total_cut += cut
            
                # Reset the days counter
                days = 0
            else:
                # Return the maximum value of d
                return days
        else:
            # Increment the days counter
            days += 1
    
    # Return the maximum value of d
    return days

