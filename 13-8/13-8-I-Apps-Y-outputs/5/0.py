
def can_construct_square(n, m, tiles):
    # Check if the number of tiles is greater than the number of cells in the square
    if len(tiles) > m ** 2:
        return "NO"
    
    # Check if the tiles are symmetric
    for i in range(n):
        for j in range(i + 1, n):
            if tiles[i][0] != tiles[j][1] or tiles[i][1] != tiles[j][0]:
                return "NO"
    
    # Check if the tiles can be placed to form a symmetric square
    for i in range(m):
        for j in range(i + 1, m):
            found = False
            for k in range(n):
                if tiles[k][0] == m ** 2 - i * m - j and tiles[k][1] == m ** 2 - i * m - i:
                    found = True
                    break
            if not found:
                return "NO"
    
    return "YES"

