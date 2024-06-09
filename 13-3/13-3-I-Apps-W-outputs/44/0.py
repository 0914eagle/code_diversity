
def get_max_cuts(n, B, a):
    # Sort the array in non-decreasing order
    a.sort()
    
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    
    # Loop through each element in the array
    for i in range(n):
        # Check if the current element is odd
        if a[i] % 2 == 1:
            # If the current element is odd, find the next even element
            for j in range(i+1, n):
                if a[j] % 2 == 0:
                    # If an even element is found, calculate the cost of the cut
                    cost = abs(a[i] - a[j])
                    
                    # Check if the cost is less than or equal to the budget
                    if cost <= B:
                        # If the cost is less than or equal to the budget, increment the maximum number of cuts
                        max_cuts += 1
                        
                        # Break out of the inner loop
                        break
    
    # Return the maximum number of cuts
    return max_cuts

