
def solve(n, distances):
    # Initialize the two subsets with the first shipment
    subset1 = [0]
    subset2 = [i for i in range(1, n)]
    
    # Iterate through the remaining shipments
    for i in range(1, n):
        # Find the subset with the smallest disparity
        if len(subset1) == 1:
            subset = subset2
        else:
            subset = subset1 if sum(distances[i][j] for j in subset1) < sum(distances[i][j] for j in subset2) else subset2
        
        # Add the current shipment to the subset
        subset.append(i)
    
    # Return the minimum possible sum of disparities
    return sum(max(distances[i][j] for j in subset1) for i in subset1) + sum(max(distances[i][j] for j in subset2) for i in subset2)

