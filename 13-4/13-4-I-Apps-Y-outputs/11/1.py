
def can_construct_square(n, m, tiles):
    # Check if the square is symmetric
    for i in range(m):
        for j in range(i+1, m):
            if tiles[i][j] != tiles[j][i]:
                return "NO"
    
    # Check if the square is possible to construct
    for i in range(m):
        for j in range(m):
            # Check if the current cell is covered
            if tiles[i][j] == 0:
                return "NO"
    
    return "YES"

