
def find_center(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    top, bottom, left, right = 0, n-1, 0, m-1
    
    # Find the first black cell
    for i in range(n):
        for j in range(m):
            if table[i][j] == "B":
                top, bottom, left, right = i, i, j, j
                break
    
    # Expand the search area
    while top - 1 >= 0 and table[top-1][left] == "B":
        top -= 1
    while bottom + 1 < n and table[bottom+1][left] == "B":
        bottom += 1
    while left - 1 >= 0 and table[top][left-1] == "B":
        left -= 1
    while right + 1 < m and table[top][right+1] == "B":
        right += 1
    
    # Find the center of the black square
    center_row = (top + bottom) // 2
    center_col = (left + right) // 2
    
    return center_row, center_col

