
def solve(a):
    # Convert the input matrix to a numpy array for easier processing
    a = np.array(a)
    
    # Initialize a variable to store the minimum number of cells to change
    min_changes = 0
    
    # Loop through each even length square sub-matrix
    for r1 in range(a.shape[0]):
        for r2 in range(r1 + 1, a.shape[0]):
            for c1 in range(a.shape[1]):
                for c2 in range(c1 + 1, a.shape[1]):
                    # Check if the sub-matrix is even length square
                    if (r2 - r1) % 2 == 0 and (c2 - c1) % 2 == 0:
                        # Count the number of ones in the sub-matrix
                        num_ones = np.sum(a[r1:r2+1, c1:c2+1])
                        # Check if the number of ones is odd
                        if num_ones % 2 == 1:
                            # Increment the minimum number of cells to change
                            min_changes += 1
    
    # Return the minimum number of cells to change
    return min_changes

