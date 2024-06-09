
def get_max_days(n, k, a):
    # Initialize variables
    days = 0
    total_length = 0
    
    # Loop through each bamboo
    for i in range(n):
        # Check if the bamboo has reached the required height
        if a[i] <= days:
            # Calculate the length of the part to be cut off
            length = days - a[i]
            
            # Check if the total length of cut parts will exceed the maximum allowed
            if total_length + length > k:
                # Return the current value of days
                return days
            else:
                # Increment the total length of cut parts
                total_length += length
        
        # Increment the number of days
        days += 1
    
    # Return the maximum value of days
    return days

