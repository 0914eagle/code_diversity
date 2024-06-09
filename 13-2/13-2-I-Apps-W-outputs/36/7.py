
def solve(N, M, bridges):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, M + 1)}
    
    # Iterate through each bridge and calculate the inconvenience after it collapses
    for i in range(1, M):
        # Get the indices of the islands connected by the bridge
        island1, island2 = bridges[i]
        
        # Iterate through the remaining bridges and check if they connect the same two islands
        for j in range(i + 1, M):
            # If the bridge connects the same two islands, increment the inconvenience
            if bridges[j][0] == island1 and bridges[j][1] == island2:
                inconvenience[i + 1] += 1
            elif bridges[j][0] == island2 and bridges[j][1] == island1:
                inconvenience[i + 1] += 1
    
    return [inconvenience[i] for i in range(1, M + 1)]

