
def can_construct_square(n, m, tiles):
    # Check if the square is symmetric
    if m != n:
        return "NO"
    
    # Check if the tiles are valid
    for i in range(n):
        for j in range(i+1, n):
            if tiles[i][0] == tiles[j][1] and tiles[i][1] == tiles[j][0]:
                return "NO"
    
    # Check if the tiles can be placed to form a square
    for i in range(n):
        for j in range(i+1, n):
            if tiles[i][0] == tiles[j][1] and tiles[i][1] == tiles[j][0]:
                return "NO"
    
    return "YES"

