
def solve(n, m):
    # Initialize the coloring as a 2D array of characters
    coloring = [['A' for _ in range(m)] for _ in range(n)]
    
    # Loop through each row of the coloring
    for i in range(n):
        # Loop through each column of the coloring
        for j in range(m):
            # If the current cell is not the first cell in its row
            if j > 0:
                # Set the color of the current cell to be the same as the previous cell
                coloring[i][j] = coloring[i][j-1]
            # If the current cell is the first cell in its row
            else:
                # Set the color of the current cell to be the next available color in alphabetical order
                coloring[i][j] = chr(ord('A') + (i * m) + j)
    
    # Return the lexicographically minimum coloring
    return "".join("".join(row) for row in coloring)

