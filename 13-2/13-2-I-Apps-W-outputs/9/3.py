
def solve(n, m):
    # Initialize the coloring matrix
    coloring = [["" for _ in range(m)] for _ in range(n)]
    
    # Fill the first row with the lexicographically minimum coloring
    for i in range(m):
        coloring[0][i] = "A"
    
    # Fill the remaining rows
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                coloring[i][j] = chr(ord(coloring[i-1][j]) + 1)
            else:
                coloring[i][j] = coloring[i-1][j]
    
    # Return the coloring
    return ["".join(row) for row in coloring]

