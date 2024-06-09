
def can_tile(n, board):
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
    # Check if the set of tiles is a subset of the set of pieces
    return tiles.issubset(pieces)

def main():
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    if can_tile(n, board):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

