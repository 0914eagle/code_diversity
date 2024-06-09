
import math

def solve(n, m, mod, matrix):
    # Calculate the number of possible rows and columns
    num_rows = int(math.pow(2, n))
    num_cols = int(math.pow(2, n))
    
    # Initialize a dictionary to store the number of special matrices for each row
    row_count = {}
    
    # Iterate over the given rows
    for i in range(m):
        # Get the current row
        current_row = matrix[i]
        
        # Initialize a set to store the unique columns for the current row
        unique_cols = set()
        
        # Iterate over the columns in the current row
        for j in range(n):
            # If the current column is 1, add it to the set of unique columns
            if current_row[j] == "1":
                unique_cols.add(j)
        
        # If the set of unique columns is not empty, add it to the dictionary
        if unique_cols:
            row_count[i] = unique_cols
    
    # Initialize a variable to store the total number of special matrices
    total_count = 0
    
    # Iterate over the dictionary of rows
    for row, cols in row_count.items():
        # Initialize a variable to store the number of special matrices for the current row
        count = 1
        
        # Iterate over the columns in the current row
        for col in cols:
            # If the column is not in the set of unique columns for any other row, add it to the count
            if col not in row_count.values():
                count *= 2
        
        # Add the count for the current row to the total count
        total_count += count
    
    # Return the remainder after dividing the total count by the modulus
    return total_count % mod

