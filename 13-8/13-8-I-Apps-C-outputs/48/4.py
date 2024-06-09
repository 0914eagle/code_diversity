
def solve(n, distances):
    # Initialize the two subsets with the first shipment
    subset1 = [0]
    subset2 = [i for i in range(1, n)]
    
    # Iterate through the remaining shipments
    for i in range(1, n):
        # Find the subset with the smallest disparity
        if D(subset1) < D(subset2):
            subset1.append(i)
        else:
            subset2.append(i)
    
    # Return the minimum possible sum of disparities
    return D(subset1) + D(subset2)

# Define the disparity function
def D(subset):
    disparity = 0
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            disparity = max(disparity, distances[subset[i]][subset[j]])
    return disparity

