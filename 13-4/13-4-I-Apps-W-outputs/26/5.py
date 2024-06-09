
def get_happy_seconds(n, x, y, c):
    # Initialize a 2D array to represent the table
    table = [[0] * n for _ in range(n)]
    
    # Set the initial cell to 1
    table[x - 1][y - 1] = 1
    
    # Iterate through each second
    for second in range(1, n * n + 1):
        # Find all cells that are off but have at least one on side-adjacent cell
        off_cells = []
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0 and any(table[k][l] == 1 for k in range(max(i - 1, 0), min(i + 2, n)) for l in range(max(j - 1, 0), min(j + 2, n))):
                    off_cells.append((i + 1, j + 1))
        
        # Switch on all found cells
        for cell in off_cells:
            table[cell[0] - 1][cell[1] - 1] = 1
        
        # Check if the condition is fulfilled
        if sum(map(sum, table)) >= c:
            return second
    
    # If the condition is not fulfilled, return -1
    return -1

