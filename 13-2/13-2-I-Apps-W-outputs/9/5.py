
def solve(n, m):
    # Initialize the coloring matrix
    coloring = [[0] * m for _ in range(n)]
    
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the cell is not painted, paint it with the next available color
            if coloring[i][j] == 0:
                coloring[i][j] = chr(ord('A') + (i * m + j) % 26)
    
    # Return the lexicographically minimum coloring
    return "".join("".join(map(str, row)) for row in coloring)

