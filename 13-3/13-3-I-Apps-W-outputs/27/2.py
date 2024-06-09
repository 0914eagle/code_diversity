
def solve(n, m, mod, matrix):
    # Initialize a dictionary to store the number of ones in each row and column
    rows = [0] * n
    cols = [0] * n
    
    # Iterate through the given matrix
    for i in range(m):
        for j in range(n):
            # If the current cell is one, increment the number of ones in the corresponding row and column
            if matrix[i][j] == "1":
                rows[i] += 1
                cols[j] += 1
    
    # Initialize a variable to store the number of special matrices
    count = 0
    
    # Iterate through the rows and columns
    for i in range(n):
        for j in range(n):
            # If the current cell is one and the number of ones in the corresponding row and column is 2, increment the count
            if matrix[i][j] == "1" and rows[i] == 2 and cols[j] == 2:
                count += 1
    
    # Return the remainder after dividing the count by the given modulus
    return count % mod

