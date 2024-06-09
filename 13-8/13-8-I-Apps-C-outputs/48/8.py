
def solve(n, distances):
    # Initialize the disparities for each subset
    disparity_A = 0
    disparity_B = 0
    
    # Loop through each shipment and calculate the disparity for each subset
    for i in range(n):
        for j in range(i+1, n):
            if i in subset_A and j in subset_A:
                disparity_A += distances[i][j]
            elif i in subset_B and j in subset_B:
                disparity_B += distances[i][j]
    
    # Return the minimum possible sum of disparities
    return disparity_A + disparity_B

