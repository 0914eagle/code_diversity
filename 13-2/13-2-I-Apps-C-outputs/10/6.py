
def get_maximum_participants(n, k, x):
    # Sort the preferences in descending order
    x.sort(reverse=True)
    
    # Initialize the maximum number of participants that can join
    max_participants = 0
    
    # Iterate through the preferences and check if the current participant can join
    for i in range(n):
        # Check if the current participant has a preference that is already in the group
        if x[i] in x[:i]:
            # If the current participant has a preference that is already in the group, they cannot join
            continue
        # Check if the current participant's preference is within the capacity of the bus
        if x[i] <= k:
            # If the current participant's preference is within the capacity of the bus, they can join
            max_participants += 1
    
    return max_participants

