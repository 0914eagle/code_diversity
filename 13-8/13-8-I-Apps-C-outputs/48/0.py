
def solve(distances):
    # Calculate the maximum distance between any two shipments
    max_distance = max([max(row) for row in distances])
    
    # Initialize the minimum disparity to a large value
    min_disparity = 10**9
    
    # Iterate over all possible subsets of shipments
    for i in range(1, len(distances) + 1):
        for subset in combinations(range(len(distances)), i):
            # Calculate the disparity of the current subset
            disparity = max([max(distances[i][j] for i in subset) for j in subset])
            
            # Check if the current disparity is less than the minimum disparity
            if disparity < min_disparity:
                min_disparity = disparity
    
    # Return the minimum disparity
    return min_disparity

