
def find_center(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    top, bottom, left, right = 0, n-1, 0, m-1
    
    # Iterate through the table and find the first black cell
    for i in range(n):
        for j in range(m):
            if table[i][j] == "B":
                top, bottom, left, right = i, i, j, j
                break
        if top != 0:
            break
    
    # Find the center of the black square
    center_row = (top + bottom) // 2
    center_col = (left + right) // 2
    
    return center_row, center_col

