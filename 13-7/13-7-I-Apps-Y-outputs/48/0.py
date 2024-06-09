
def can_construct_symmetric_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"
    for i in range(n):
        if len(tiles[2 * i]) != 2 or len(tiles[2 * i + 1]) != 2:
            return "NO"
        for j in range(2):
            if not tiles[2 * i][j].isdigit() or not tiles[2 * i + 1][j].isdigit():
                return "NO"
            num = int(tiles[2 * i][j]) + int(tiles[2 * i + 1][j])
            if num > 100:
                return "NO"
    
    # Check if the square is symmetric
    for i in range(m):
        for j in range(i + 1, m):
            if tiles[i][j] != tiles[j][i]:
                return "NO"
    
    # Check if the square can be constructed
    for i in range(m):
        for j in range(m):
            found = False
            for k in range(n):
                if tiles[i][j] == tiles[k][k]:
                    found = True
                    break
            if not found:
                return "NO"
    
    return "YES"

