
def solve(n, m):
    # Initialize the coloring matrix
    coloring = [["" for _ in range(m)] for _ in range(n)]
    
    # Fill the first row with the first two colors
    coloring[0][0] = "A"
    coloring[0][1] = "B"
    
    # Fill the remaining rows
    for i in range(1, n):
        for j in range(m):
            if j % 2 == 0:
                coloring[i][j] = "A"
            else:
                coloring[i][j] = "B"
    
    # Return the lexicographically minimum coloring
    return ["".join(row) for row in coloring]

