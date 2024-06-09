
def can_construct_square(n, m, tiles):
    # Check if the square is valid
    if m != n:
        return "NO"
    
    # Check if all tiles are valid
    for tile in tiles:
        if tile[0] > m or tile[1] > m:
            return "NO"
    
    # Check if the tiles are symmetric
    for i in range(n):
        for j in range(i+1, n):
            if tiles[i][0] != tiles[j][1] or tiles[i][1] != tiles[j][0]:
                return "NO"
    
    # Check if the tiles can be placed to form a symmetric square
    for i in range(n):
        for j in range(i+1, n):
            if tiles[i][0] == tiles[j][1] and tiles[i][1] == tiles[j][0]:
                return "YES"
    
    return "NO"

