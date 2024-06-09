
def solve(n, distances):
    # Initialize the disparities of both subsets as infinite
    disparity_a = float('inf')
    disparity_b = float('inf')
    
    # Initialize the subsets as empty
    subset_a = []
    subset_b = []
    
    # Iterate over each distance
    for i in range(n):
        for j in range(i+1, n):
            # If the distance is less than the current disparity of either subset,
            # update the disparity and the subset accordingly
            if distances[i][j] < disparity_a:
                disparity_a = distances[i][j]
                subset_a = [i, j]
            elif distances[i][j] < disparity_b:
                disparity_b = distances[i][j]
                subset_b = [i, j]
    
    # Return the sum of the disparities
    return disparity_a + disparity_b

