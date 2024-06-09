
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
            # If the current tile has not been used, try to use it to cover five cells
            if (i, j) not in used_tiles:
                # Get the positions of the cells covered by the current tile
                covered_cells = get_covered_cells(n, (i, j), tiles)
                # If the current tile covers five distinct cells and no two tiles overlap, add it to the set of used tiles and continue to the next tile
                if len(covered_cells) == 5 and not any(tile in used_tiles for tile in covered_cells):
                    used_tiles.update(covered_cells)
                    continue
                # If the current tile does not cover five distinct cells or overlaps with another tile, return False
                return False
    # If all tiles have been used, return True
    return True

def get_covered_cells(n, tile_position, tiles):
    # Get the row and column of the current tile
    row, col = tile_position
    # Initialize a set to store the positions of the cells covered by the current tile
    covered_cells = set()
    # Iterate over the four cells adjacent to the current tile
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # If the current cell is free and is not the current tile, add it to the set of covered cells
            if (i, j) in tiles and (i, j) != tile_position:
                covered_cells.add((i, j))
    return covered_cells

if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    print(can_tile_board(n, board))

