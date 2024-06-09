
def solve(n, m, table):
    # Initialize the center row and column
    center_row, center_col = 0, 0
    
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current cell is black, update the center row and column
            if table[i][j] == "B":
                center_row = i
                center_col = j
                break
    
    return center_row, center_col

