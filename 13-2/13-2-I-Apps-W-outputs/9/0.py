
def solve(n, m):
    # Initialize the coloring as a 2D array of characters
    coloring = [['A' for _ in range(m)] for _ in range(n)]
    
    # Loop through each row of the coloring
    for i in range(n):
        # Loop through each column of the coloring
        for j in range(m):
            # If the current cell is not the first cell in its row, check if the previous cell has the same color
            if j > 0 and coloring[i][j-1] == coloring[i][j]:
                # If the previous cell has the same color, change the current cell to the next letter in the alphabet
                coloring[i][j] = chr(ord(coloring[i][j]) + 1)
    
    # Return the lexicographically minimum coloring
    return "".join("".join(row) for row in coloring)

