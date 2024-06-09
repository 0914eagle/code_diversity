
def f1(n, board):
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
            # If the current tile has not been used, try to use it to cover the board
            if (i, j) not in used_tiles:
                # Check if the current tile can be used to cover the board
                if can_cover_board(n, board, tiles, used_tiles, (i, j)):
                    # If it can, return YES
                    return "YES"
    
    # If no tile can be used to cover the board, return NO
    return "NO"

def can_cover_board(n, board, tiles, used_tiles, pos):
    # If the current tile has already been used, return False
    if pos in used_tiles:
        return False
    
    # Add the current tile to the set of used tiles
    used_tiles.add(pos)
    
    # Initialize a set to store the positions of the tiles that are adjacent to the current tile
    adjacent_tiles = set()
    
    # Iterate over the tiles that are adjacent to the current tile
    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1] - 1, pos[1] + 2):
            # If the current tile is within the board and is not the current tile, add it to the set of adjacent tiles
            if 0 <= i < n and 0 <= j < n and (i, j) != pos and (i, j) in tiles:
                adjacent_tiles.add((i, j))
    
    # If all of the adjacent tiles have been used, return True
    if len(adjacent_tiles) == 4:
        return True
    
    # Otherwise, try to use each of the adjacent tiles to cover the board
    for tile in adjacent_tiles:
        if can_cover_board(n, board, tiles, used_tiles, tile):
            return True
    
    # If no adjacent tile can be used to cover the board, return False
    return False

if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    print(f1(n, board))

