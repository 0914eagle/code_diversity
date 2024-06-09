
def solve(n, m, bridges):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, m + 1)}
    
    # Iterate through each bridge and calculate the inconvenience after it collapses
    for i in range(1, m + 1):
        # Get the indices of the islands connected by the bridge
        island1, island2 = bridges[i - 1]
        
        # Iterate through the remaining bridges and check if they connect the same islands
        for j in range(i + 1, m + 1):
            # If the bridge connects the same islands, increment the inconvenience
            if bridges[j - 1][0] == island1 and bridges[j - 1][1] == island2:
                inconvenience[i] += 1
            elif bridges[j - 1][0] == island2 and bridges[j - 1][1] == island1:
                inconvenience[i] += 1
    
    return [inconvenience[i] for i in range(1, m + 1)]

