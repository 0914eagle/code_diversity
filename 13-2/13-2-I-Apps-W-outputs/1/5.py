
def solve(a):
    # Convert the input matrix to a numpy array for easy indexing
    a = np.array(a)
    
    # Initialize a variable to store the minimum number of cells to change
    min_changes = float('inf')
    
    # Loop through each possible starting row and column
    for r1 in range(a.shape[0]):
        for c1 in range(a.shape[1]):
            # Calculate the number of rows and columns in the current sub-matrix
            r2 = r1 + (a.shape[0] - r1) // 2
            c2 = c1 + (a.shape[1] - c1) // 2
            
            # Check if the current sub-matrix is even length square
            if (r2 - r1) % 2 == 0 and (c2 - c1) % 2 == 0:
                # Calculate the number of ones in the current sub-matrix
                num_ones = np.sum(a[r1:r2+1, c1:c2+1])
                
                # Check if the number of ones is odd
                if num_ones % 2 == 1:
                    # Calculate the number of cells to change to make the sub-matrix good
                    changes = (r2 - r1) * (c2 - c1) - num_ones
                    
                    # Update the minimum number of cells to change if necessary
                    min_changes = min(min_changes, changes)
    
    # Check if it is possible to make the matrix good
    if min_changes == float('inf'):
        return -1
    else:
        return min_changes

