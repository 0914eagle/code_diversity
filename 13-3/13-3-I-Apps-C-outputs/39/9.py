
def f1(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the number of moves
    current_player = "Mirko"
    num_moves = 0

    # Loop until a player cannot make a move
    while num_moves < N:
        # Get the current player's move
        x, y = points[num_moves]

        # Update the game board with the current player's move
        board[x][y] = 1

        # Check if the current player has won
        if check_win(board, current_player):
            return current_player

        # Switch to the other player
        current_player = "Slavko" if current_player == "Mirko" else "Mirko"

        # Increment the number of moves
        num_moves += 1

    # If all moves have been played and no player has won, it's a draw
    return "Draw"

def f2(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the number of moves
    current_player = "Slavko"
    num_moves = 0

    # Loop until a player cannot make a move
    while num_moves < N:
        # Get the current player's move
        x, y = points[num_moves]

        # Update the game board with the current player's move
        board[x][y] = 1

        # Check if the current player has won
        if check_win(board, current_player):
            return current_player

        # Switch to the other player
        current_player = "Mirko" if current_player == "Slavko" else "Slavko"

        # Increment the number of moves
        num_moves += 1

    # If all moves have been played and no player has won, it's a draw
    return "Draw"

def check_win(board, player):
    # Check rows
    for row in board:
        if all(row) and row[0] == player:
            return True

    # Check columns
    for i in range(len(board[0])):
        if all([row[i] for row in board]) and board[0][i] == player:
            return True

    # Check diagonals
    for i in range(len(board[0])):
        if all([board[i][i] for i in range(len(board[0]))]) and board[0][0] == player:
            return True
        if all([board[i][len(board[0]) - i - 1] for i in range(len(board[0]))]) and board[0][len(board[0]) - 1] == player:
            return True

    # If no player has won, return False
    return False

if __name__ == '__main__':
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    print(f1(N, points))

