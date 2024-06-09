
def solve(n, m, bridges):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, m + 1)}
    
    # Iterate through each bridge and calculate the inconvenience after it collapses
    for i in range(1, m + 1):
        # Get the indices of the islands connected by the bridge
        island1, island2 = bridges[i - 1]
        
        # Iterate through each island and check if it is connected to the other island
        for j in range(1, n + 1):
            if j != island1 and j != island2:
                # If the island is not connected to either of the islands connected by the bridge, increment the inconvenience
                inconvenience[i] += 1
    
    return inconvenience

