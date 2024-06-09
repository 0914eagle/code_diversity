
def solve(n, m, bridges):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, m + 1)}
    
    # Iterate through each bridge and calculate the inconvenience after it collapses
    for i in range(1, m + 1):
        # Get the indices of the islands connected by the bridge
        a, b = bridges[i - 1]
        
        # Iterate through each island and check if it is connected to the other island by any other bridge
        for j in range(1, n + 1):
            if j != a and j != b:
                # If the island is not connected to either of the islands connected by the bridge, increment the inconvenience
                if not any(j in bridge for bridge in bridges if bridge[0] != a and bridge[1] != b):
                    inconvenience[i] += 1
    
    return [inconvenience[i] for i in range(1, m + 1)]

