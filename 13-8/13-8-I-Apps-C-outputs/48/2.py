
def solve(distances):
    # Calculate the maximum distance between any two shipments
    max_distance = max([max(row) for row in distances])
    
    # Initialize the minimum sum of disparities to a large value
    min_sum_disparities = float('inf')
    
    # Iterate over all possible subsets of shipments
    for i in range(1, len(distances) + 1):
        for subset in combinations(range(len(distances)), i):
            # Calculate the disparity of the current subset
            disparity = max([max(distances[i][j] for i in subset) for j in subset])
            
            # If the disparity is less than the minimum sum of disparities, update the minimum sum of disparities
            if disparity < min_sum_disparities:
                min_sum_disparities = disparity
    
    # Return the minimum sum of disparities
    return min_sum_disparities

