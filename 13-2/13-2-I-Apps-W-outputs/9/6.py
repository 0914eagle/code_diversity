
def solve(n, m):
    # Initialize the coloring matrix
    coloring = [["" for _ in range(m)] for _ in range(n)]

    # Fill the first row with the lexicographically minimum coloring
    for i in range(m):
        coloring[0][i] = "A"

    # Fill the remaining rows
    for i in range(1, n):
        for j in range(m):
            # If the cell is in the first column, use the next lexicographically minimum color
            if j == 0:
                coloring[i][j] = chr(ord(coloring[i-1][j]) + 1)
            # If the cell is in the first row, use the same color as the cell above
            elif i == 0:
                coloring[i][j] = coloring[i][j-1]
            # If the cell is in both the first row and column, use the next lexicographically minimum color
            else:
                coloring[i][j] = chr(ord(coloring[i-1][j]) + 1)
                if coloring[i][j] == coloring[i][j-1]:
                    coloring[i][j] = chr(ord(coloring[i][j]) + 1)

    # Return the coloring matrix
    return coloring

