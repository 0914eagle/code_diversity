
def get_max_days(n, k, a):
    # Initialize variables
    days = 0
    total_length = 0
    
    # Loop through each bamboo
    for i in range(n):
        # Check if the bamboo has reached the required height
        if a[i] <= days:
            # Calculate the length of the cut part
            length = days - a[i]
            
            # Check if the total length of cut parts is less than or equal to k
            if total_length + length <= k:
                # Increment the total length of cut parts
                total_length += length
            
            # Cut the bamboo
            a[i] = days
    
    # Return the maximum value of d
    return days

