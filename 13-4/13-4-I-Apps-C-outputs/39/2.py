
def max_frogs_that_can_escape(n, d, frogs):
    # Sort the frogs in descending order of their leap capacity
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaping_frogs = 0
    
    # Iterate through the frogs and check if they can escape the pit
    for frog in frogs:
        # Check if the frog's leap capacity is greater than the depth of the pit
        if frog[0] > d:
            # Increment the maximum number of escaping frogs
            max_escaping_frogs += 1
        # Check if the frog can be carried by another frog
        elif frog[1] < d:
            # Find the first frog that can carry the current frog
            for i in range(n):
                if frogs[i][0] > d - frog[1]:
                    # Increment the maximum number of escaping frogs
                    max_escaping_frogs += 1
                    break
    
    return max_escaping_frogs

