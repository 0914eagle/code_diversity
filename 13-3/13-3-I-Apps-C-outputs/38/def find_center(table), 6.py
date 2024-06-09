
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
    
    # Expand the search area until the whole square is found
    while top > 0 and table[top-1][left] == "W":
        top -= 1
    while bottom < n-1 and table[bottom+1][left] == "W":
        bottom += 1
    while left > 0 and table[top][left-1] == "W":
        left -= 1
    while right < m-1 and table[top][right+1] == "W":
        right += 1
    
    # Return the center of the square
    return (top + bottom) // 2 + 1, (left + right) // 2 + 1

