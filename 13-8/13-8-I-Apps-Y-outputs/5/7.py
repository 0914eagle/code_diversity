
def can_construct_symmetric_square(n, m, tiles):
    # Check if the square is symmetric
    for i in range(m):
        for j in range(i+1, m):
            if tiles[i][j] != tiles[j][i]:
                return "NO"
    
    # Check if the square can be constructed with the given tiles
    for i in range(m):
        for j in range(i+1, m):
            found = False
            for k in range(n):
                if tiles[i][j] == tiles[i][k] and tiles[j][i] == tiles[k][j]:
                    found = True
                    break
            if not found:
                return "NO"
    
    return "YES"

