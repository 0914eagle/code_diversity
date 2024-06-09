
def can_tile_board(n, board):
    # Initialize a set to store the positions of the tiles
    tiles = set()
    # Iterate over the board
    for i in range(n):
        for j in range(n):
            # If the current cell is free, add it to the set of tiles
            if board[i][j] == ".":
                tiles.add((i, j))
    # Initialize a set to store the positions of the pieces
    pieces = set()
    # Iterate over the pieces
    for i in range(n):
        for j in range(n):
            # If the current cell is part of a piece, add it to the set of pieces
            if board[i][j] == "#":
                pieces.add((i, j))
    # Initialize a variable to store the number of tiles used
    num_tiles = 0
    # Iterate over the tiles
    for i in range(n):
        for j in range(n):
            # If the current tile is not part of a piece, increment the number of tiles used
            if (i, j) not in pieces:
                num_tiles += 1
    # If the number of tiles used is equal to the number of tiles available, return YES
    if num_tiles == len(tiles):
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

def main():
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    print(can_tile_board(n, board))

if __name__ == '__main__':
    main()

