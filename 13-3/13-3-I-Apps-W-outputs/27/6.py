
import math

def solve(n, m, mod, matrix):
    # Initialize the number of special matrices to 0
    num_special_matrices = 0
    
    # Loop over each row of the matrix
    for i in range(m):
        # Get the number of ones in the current row
        num_ones = matrix[i].count('1')
        
        # Check if the number of ones is equal to 2
        if num_ones == 2:
            # Increment the number of special matrices
            num_special_matrices += 1
        
    # Return the remainder after dividing the number of special matrices by the given modulus
    return num_special_matrices % mod

