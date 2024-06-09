
def solve(n, d, frogs):
    # Sort the frogs by their leap capacity in descending order
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaped = 0
    
    # Loop through each frog and check if it can escape the pit
    for frog in frogs:
        # Check if the frog's leap capacity is greater than the depth of the pit
        if frog[0] > d:
            # Increment the maximum number of frogs that can escape
            max_escaped += 1
        # Check if the frog can be carried by another frog
        elif frog[1] < d:
            # Loop through the remaining frogs and check if any of them can carry the frog
            for other_frog in frogs:
                # Check if the other frog's leap capacity is greater than the depth of the pit
                if other_frog[0] > d:
                    # Check if the other frog's weight plus the frog's weight is less than or equal to the depth of the pit
                    if other_frog[1] + frog[1] <= d:
                        # Increment the maximum number of frogs that can escape
                        max_escaped += 1
                        # Break out of the loop since we have found a frog that can carry the current frog
                        break
    
    # Return the maximum number of frogs that can escape
    return max_escaped
