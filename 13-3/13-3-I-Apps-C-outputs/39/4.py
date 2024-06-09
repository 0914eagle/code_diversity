
def f1(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the number of moves
    current_player = "Mirko"
    num_moves = 0

    # Loop until a winner is determined
    while True:
        # Get the current player's move
        x, y = points[num_moves]

        # Update the game board with the current player's move
        board[x][y] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            return current_player

        # Update the current player and number of moves
        current_player = "Slavko" if current_player == "Mirko" else "Mirko"
        num_moves += 1

        # Check if the game has ended in a draw
        if num_moves == N:
            return "Draw"

def f2(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the number of moves
    current_player = "Slavko"
    num_moves = 0

    # Loop until a winner is determined
    while True:
        # Get the current player's move
        x, y = points[num_moves]

        # Update the game board with the current player's move
        board[x][y] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            return current_player

        # Update the current player and number of moves
        current_player = "Mirko" if current_player == "Slavko" else "Slavko"
        num_moves += 1

        # Check if the game has ended in a draw
        if num_moves == N:
            return "Draw"

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == len(row):
            return True

    # Check columns
    for i in range(len(board[0])):
        if [row[i] for row in board].count(player) == len(board):
            return True

    # Check diagonals
    for i in range(len(board)):
        if [board[i][i] for i in range(len(board[0]))].count(player) == len(board):
            return True
        if [board[i][len(board[0]) - i - 1] for i in range(len(board[0]))].count(player) == len(board):
            return True

    return False

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    print(f1(N, points))

