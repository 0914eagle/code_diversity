
def f1(N, points):
    # Initialize the board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Set the starting point
    board[1][1] = 1

    # Iterate through the moves
    for i in range(2, N + 1):
        # Get the previous move
        prev_x, prev_y = points[i - 2]

        # Find the next move
        for x in range(1, N + 1):
            if board[prev_x][x] == 0 and board[x][prev_y] == 0:
                break

        # Make the move
        board[prev_x][x] = 1
        board[x][prev_y] = 1

    # Check if Mirko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 0:
                return "Mirko"

    return "Slavko"

def f2(N, points):
    # Initialize the board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Set the starting point
    board[1][1] = 1

    # Iterate through the moves
    for i in range(2, N + 1):
        # Get the previous move
        prev_x, prev_y = points[i - 2]

        # Find the next move
        for y in range(1, N + 1):
            if board[prev_x][y] == 0 and board[y][prev_y] == 0:
                break

        # Make the move
        board[prev_x][y] = 1
        board[y][prev_y] = 1

    # Check if Slavko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 0:
                return "Slavko"

    return "Mirko"

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    print(f1(N, points))

