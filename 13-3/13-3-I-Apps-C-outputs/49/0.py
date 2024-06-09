
def solve_magic_checkerboard(checkerboard):
    # Initialize variables
    n, m = len(checkerboard), len(checkerboard[0])
    rows, cols = [[] for _ in range(n)], [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] != 0:
                rows[i].append(checkerboard[i][j])
                cols[j].append(checkerboard[i][j])
    
    # Check if the checkerboard is valid
    for i in range(n):
        for j in range(m-1):
            if rows[i][j] >= rows[i][j+1] or cols[j][i] >= cols[j+1][i]:
                return -1
    
    # Fill in the remaining cells
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] == 0:
                checkerboard[i][j] = min(rows[i][-1], cols[j][-1]) + 1
    
    # Calculate the sum
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += checkerboard[i][j]
    
    return sum

