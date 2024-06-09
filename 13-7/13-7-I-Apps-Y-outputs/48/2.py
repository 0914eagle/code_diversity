
def can_construct_symmetric_matrix(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a 2D array to store the tiles
    matrix = [[0 for _ in range(m)] for _ in range(m)]

    # Iterate through each tile type
    for i in range(n):
        # Get the current tile type
        tile = tiles[2 * i]
        # Get the top and bottom numbers of the current tile type
        top, bottom = tile[0], tile[1]
        # Get the left and right numbers of the current tile type
        left, right = tile[2], tile[3]
        # Check if the current tile type can be placed in the matrix
        for j in range(m):
            for k in range(m):
                # Check if the current tile type can be placed in the (j, k) position
                if matrix[j][k] == 0 and (j == 0 or matrix[j - 1][k] == top) and (k == 0 or matrix[j][k - 1] == left):
                    # Place the current tile type in the (j, k) position
                    matrix[j][k] = i + 1
                    # Check if the current tile type forms a symmetric matrix
                    for l in range(m):
                        if matrix[j][l] != matrix[l][k]:
                            break
                    else:
                        return "YES"
                    # If the current tile type does not form a symmetric matrix, undo the placement
                    matrix[j][k] = 0

    # If no symmetric matrix can be formed, return "NO"
    return "NO"

