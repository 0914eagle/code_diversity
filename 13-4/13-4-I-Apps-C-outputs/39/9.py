
def max_frogs_can_escape(n, d, frogs):
    # Sort the frogs in descending order of their leap capacity
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaping_frogs = 0
    
    # Loop through each frog and check if it can escape the pit
    for frog in frogs:
        # Check if the frog's leap capacity is greater than the depth of the pit
        if frog[0] > d:
            # Increment the maximum number of escaping frogs
            max_escaping_frogs += 1
        # Check if the frog can be carried by another frog
        elif frog[1] < d:
            # Loop through the remaining frogs and check if any of them can carry the frog
            for i in range(n):
                # Check if the current frog is not the same as the frog being checked
                if i != frog[2]:
                    # Check if the current frog's leap capacity is greater than the sum of the frog being checked's leap capacity and height
                    if frogs[i][0] > frog[0] + frog[2]:
                        # Increment the maximum number of escaping frogs
                        max_escaping_frogs += 1
                        # Break out of the loop
                        break
    
    # Return the maximum number of escaping frogs
    return max_escaping_frogs

