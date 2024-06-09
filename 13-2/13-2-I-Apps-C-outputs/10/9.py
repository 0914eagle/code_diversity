
def get_maximum_participants(n, k, x):
    # Sort the preferences in descending order
    x.sort(reverse=True)
    
    # Initialize the maximum number of participants that can join
    max_participants = 0
    
    # Iterate through the preferences and check if the current participant can join
    for i in range(n):
        # Check if the current participant has a preference that is not already satisfied
        if x[i] > max_participants:
            # Check if the current participant's preference is within the bus capacity
            if x[i] <= k:
                # Increment the maximum number of participants that can join
                max_participants += 1
            else:
                # Break the loop if the current participant's preference is not within the bus capacity
                break
    
    return max_participants

