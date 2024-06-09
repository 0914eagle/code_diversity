
def can_construct_square(n, m, tiles):
    # Check if the square is symmetric
    for i in range(m):
        for j in range(i+1, m):
            if tiles[i][j] != tiles[j][i]:
                return "NO"
    
    # Check if the square is filled with tiles
    for i in range(m):
        for j in range(m):
            if tiles[i][j] == 0:
                return "NO"
    
    # Check if the tiles are placed correctly
    for i in range(m):
        for j in range(m):
            if i > 0 and tiles[i][j] == tiles[i-1][j]:
                return "NO"
            if j > 0 and tiles[i][j] == tiles[i][j-1]:
                return "NO"
    
    return "YES"

