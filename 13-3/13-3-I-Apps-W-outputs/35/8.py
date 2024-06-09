
def can_tile_board(n, board):
    # Initialize a set to store the positions of the tiles
    tiles = set()
    # Iterate over the board
    for i in range(n):
        for j in range(n):
            # If the current cell is free, add it to the set of tiles
            if board[i][j] == ".":
                tiles.add((i, j))
    # Initialize a set to store the positions of the tiles that have been used
    used_tiles = set()
    # Iterate over the tiles
    for i in range(n):
        for j in range(n):
            # If the current tile has not been used, try to use it to tile the board
            if (i, j) not in used_tiles:
                # Check if the current tile can be used to tile the board
                if can_tile_board_with_tile(n, board, tiles, used_tiles, (i, j)):
                    # If it can be used, return True
                    return True
    # If no tile can be used to tile the board, return False
    return False

def can_tile_board_with_tile(n, board, tiles, used_tiles, tile_position):
    # Add the current tile to the set of used tiles
    used_tiles.add(tile_position)
    # Get the positions of the cells that the current tile covers
    tile_cells = get_tile_cells(n, tile_position)
    # Check if the current tile covers all the cells of the board
    if len(tile_cells) == n ** 2:
        return True
    # Iterate over the tiles that have not been used
    for tile_position in tiles - used_tiles:
        # Check if the current tile can be used to tile the board with the current tile
        if can_tile_board_with_tile(n, board, tiles, used_tiles, tile_position):
            # If it can be used, return True
            return True
    # If no tile can be used to tile the board with the current tile, return False
    return False

def get_tile_cells(n, tile_position):
    # Get the row and column of the current tile
    row, col = tile_position
    # Initialize a set to store the positions of the cells that the current tile covers
    tile_cells = set()
    # Iterate over the cells that the current tile covers
    for i in range(row, row + 5):
        for j in range(col, col + 5):
            # If the current cell is within the bounds of the board, add it to the set of cells that the current tile covers
            if 0 <= i < n and 0 <= j < n:
                tile_cells.add((i, j))
    # Return the set of cells that the current tile covers
    return tile_cells

if __name__ == '__main__':
    n = int(input())
    board = [input() for _ in range(n)]
    print("YES") if can_tile_board(n, board) else print("NO")

