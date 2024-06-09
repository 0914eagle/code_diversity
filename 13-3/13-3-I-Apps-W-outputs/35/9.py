
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
                # Try to use the current tile to tile the board
                if try_tile_board(n, board, tiles, used_tiles, (i, j)):
                    # If the board can be tiled, return True
                    return True
    # If the board cannot be tiled, return False
    return False

def try_tile_board(n, board, tiles, used_tiles, pos):
    # If the current tile has already been used, return False
    if pos in used_tiles:
        return False
    # Add the current tile to the set of used tiles
    used_tiles.add(pos)
    # Get the neighbors of the current tile
    neighbors = get_neighbors(n, board, pos)
    # If there are no neighbors, return True
    if not neighbors:
        return True
    # Iterate over the neighbors
    for neighbor in neighbors:
        # If the neighbor has not been used, try to use it to tile the board
        if neighbor not in used_tiles:
            # Try to use the neighbor to tile the board
            if try_tile_board(n, board, tiles, used_tiles, neighbor):
                # If the board can be tiled, return True
                return True
    # If the board cannot be tiled, return False
    return False

def get_neighbors(n, board, pos):
    # Get the row and column of the current tile
    row, col = pos
    # Initialize a list to store the neighbors
    neighbors = []
    # Iterate over the rows and columns
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # If the current cell is a neighbor of the current tile, add it to the list of neighbors
            if 0 <= i < n and 0 <= j < n and (i, j) != pos and board[i][j] == ".":
                neighbors.append((i, j))
    # Return the list of neighbors
    return neighbors

if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    print("YES") if can_tile_board(n, board) else print("NO")

