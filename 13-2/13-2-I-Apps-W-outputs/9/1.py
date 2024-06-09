
def solve(n, m):
    # Initialize the coloring with 'A'
    coloring = ['A' for _ in range(n * m)]
    
    # Iterate through each row
    for i in range(n):
        # Iterate through each column
        for j in range(m):
            # If the cell is not in the first row or column, check if the cell above and to the left is the same color
            if i > 0 and j > 0 and coloring[i * m + j - 1] == coloring[(i - 1) * m + j]:
                # If the cell above and to the left is the same color, change the current cell to the next letter in the alphabet
                coloring[i * m + j] = chr(ord(coloring[i * m + j - 1]) + 1)
    
    return "".join(coloring)

