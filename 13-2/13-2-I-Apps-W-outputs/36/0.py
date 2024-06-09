
def solve(n, m, bridges):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, m + 1)}
    
    # Iterate through each bridge and calculate the inconvenience after it collapses
    for i in range(1, m + 1):
        # Get the indices of the islands connected by the bridge
        island1, island2 = bridges[i - 1]
        
        # Iterate through each island and calculate the inconvenience for each pair of islands
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                # If the bridge connects two islands that are not directly connected, increment the inconvenience
                if (j, k) not in [(island1, island2), (island2, island1)]:
                    inconvenience[i] += 1
    
    return [inconvenience[i] for i in range(1, m + 1)]

