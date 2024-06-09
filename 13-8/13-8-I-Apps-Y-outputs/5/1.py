
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a 2D array to store the tiles
    board = [[0] * m for _ in range(m)]

    # Loop through each tile type
    for i in range(n):
        # Get the current tile type
        tile = tiles[2 * i]
        # Check if the tile is valid
        if tile[0] < 1 or tile[0] > 100:
            return "NO"
        if tile[1] < 1 or tile[1] > 100:
            return "NO"

        # Loop through each cell in the board
        for j in range(m):
            for k in range(m):
                # Check if the current cell is empty
                if board[j][k] == 0:
                    # Check if the tile can be placed in the current cell
                    if can_place_tile(board, j, k, tile):
                        # Place the tile in the current cell
                        board[j][k] = tile
                        break

    # Check if all cells in the board are filled
    for i in range(m):
        for j in range(m):
            if board[i][j] == 0:
                return "NO"

    # Check if the board is symmetric
    for i in range(m):
        for j in range(i):
            if board[i][j] != board[j][i]:
                return "NO"

    return "YES"

def can_place_tile(board, i, j, tile):
    # Check if the tile can be placed in the current cell
    if tile[0] == board[i][j] and tile[1] == board[i][j]:
        return True
    if tile[0] == board[i][j] and tile[1] == board[j][i]:
        return True
    if tile[1] == board[i][j] and tile[0] == board[j][i]:
        return True
    return False

# Test the can_construct_square function with the example input
n = 3
m = 4
tiles = [[1, 2], [5, 6], [5, 7], [7, 4], [8, 9], [9, 8], [2, 5], [1, 1], [1, 1], [2, 2], [2, 2], [1, 100], [10, 10], [10, 10], [1, 2], [4, 5], [8, 4], [2, 2], [1, 1], [1, 1], [1, 2], [3, 4], [1, 2], [1, 1], [1, 1]]
print(can_construct_square(n, m, tiles))

# Test the can_construct_square function with other test cases
n = 2
m = 2
tiles = [[1, 2], [3, 4]]
print(can_construct_square(n, m, tiles))

n = 3
m = 3
tiles = [[1, 2], [3, 4], [5, 6]]
print(can_construct_square(n, m, tiles))

n = 2
m = 3
tiles = [[1, 2], [3, 4]]
print(can_construct_square(n, m, tiles))

n = 2
m = 2
tiles = [[1, 2], [3, 4], [5, 6]]
print(can_construct_square(n, m, tiles))

n = 2
m = 2
tiles = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(can_construct_square(n, m, tiles))

