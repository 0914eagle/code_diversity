
def is_board_tileable(n, board):
    # Initialize a set to store the positions of the tiles
    tiles = set()
    # Iterate over the board
    for i in range(n):
        for j in range(n):
            # If the current cell is free, add its position to the set of tiles
            if board[i][j] == ".":
                tiles.add((i, j))
    # Initialize a set to store the positions of the pieces
    pieces = set()
    # Iterate over the pieces
    for i in range(n):
        for j in range(n):
            # If the current cell is part of a piece, add its position to the set of pieces
            if board[i][j] == "#":
                pieces.add((i, j))
    # Check if the set of tiles is a superset of the set of pieces
    return tiles >= pieces

def main():
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())
    if is_board_tileable(n, board):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

