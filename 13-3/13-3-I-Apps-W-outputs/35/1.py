
def is_board_tileable(n, board):
    # Initialize a set to store the positions of the tiles
    tiles = set()
    # Iterate over the board
    for i in range(n):
        for j in range(n):
            # If the current cell is free, add its position to the set of tiles
            if board[i][j] == ".":
                tiles.add((i, j))
    # Initialize a set to store the positions of the tiles that have been used
    used_tiles = set()
    # Iterate over the tiles
    for i in range(n):
        for j in range(n):
            # If the current tile has not been used, try to use it to cover five cells
            if (i, j) not in used_tiles:
                # Get the positions of the cells that the current tile can cover
                covered_cells = get_covered_cells(n, (i, j), tiles)
                # If the current tile can cover five cells, mark it as used and add the covered cells to the set of used tiles
                if len(covered_cells) == 5:
                    used_tiles.add((i, j))
                    used_tiles.update(covered_cells)
    # If all tiles have been used, return YES, otherwise return NO
    if len(used_tiles) == len(tiles):
        return "YES"
    else:
        return "NO"

def get_covered_cells(n, tile_position, tiles):
    # Initialize a set to store the positions of the cells that the current tile can cover
    covered_cells = set()
    # Get the row and column of the current tile
    row, col = tile_position
    # Iterate over the four directions (up, down, left, and right)
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Initialize a set to store the positions of the cells that the current tile can cover in the current direction
        current_direction_cells = set()
        # Iterate over the cells in the current direction
        for i in range(1, n):
            # Get the position of the current cell
            current_cell = (row + i * direction[0], col + i * direction[1])
            # If the current cell is a valid position on the board and is not already covered by a tile, add it to the set of cells that the current tile can cover in the current direction
            if 0 <= current_cell[0] < n and 0 <= current_cell[1] < n and current_cell not in tiles and current_cell not in covered_cells:
                current_direction_cells.add(current_cell)
        # Add the cells that the current tile can cover in the current direction to the set of cells that the current tile can cover
        covered_cells.update(current_direction_cells)
    # Return the set of cells that the current tile can cover
    return covered_cells

if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    print(is_board_tileable(n, board))

