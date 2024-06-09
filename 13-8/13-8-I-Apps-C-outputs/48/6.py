
def solve(n, distances):
    # Initialize the disparity of each shipment as infinity
    disparity = [float('inf') for _ in range(n)]
    
    # Loop through each shipment and calculate its disparity
    for i in range(n):
        for j in range(i+1, n):
            disparity[i] = min(disparity[i], distances[i][j])
            disparity[j] = min(disparity[j], distances[i][j])
    
    # Partition the shipments into two groups based on their disparity
    group_1 = []
    group_2 = []
    for i in range(n):
        if disparity[i] % 2 == 0:
            group_1.append(i)
        else:
            group_2.append(i)
    
    # Calculate the sum of the disparities for the two groups
    disparity_1 = sum(disparity[i] for i in group_1)
    disparity_2 = sum(disparity[i] for i in group_2)
    
    # Return the minimum possible sum of disparities
    return min(disparity_1, disparity_2)

