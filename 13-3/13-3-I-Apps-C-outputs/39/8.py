
def f1(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Set the first point as the starting point
    board[1][1] = 1

    # Iterate through the points
    for i in range(2, N + 1):
        # Get the current point
        x, y = points[i - 1]

        # Find the previous point
        for j in range(1, N + 1):
            if board[j][x] == 1:
                break

        # Set the current point as the previous point
        board[j][x] = 1
        board[y][j] = 1

    # Check if Mirko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 0:
                return "Mirko"

    # Check if Slavko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[j][i] == 0:
                return "Slavko"

    # If no one has a winning strategy, return "Mirko"
    return "Mirko"

def f2(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Set the first point as the starting point
    board[1][1] = 1

    # Iterate through the points
    for i in range(2, N + 1):
        # Get the current point
        x, y = points[i - 1]

        # Find the previous point
        for j in range(1, N + 1):
            if board[j][y] == 1:
                break

        # Set the current point as the previous point
        board[j][y] = 1
        board[x][j] = 1

    # Check if Mirko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 0:
                return "Mirko"

    # Check if Slavko has a winning strategy
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[j][i] == 0:
                return "Slavko"

    # If no one has a winning strategy, return "Mirko"
    return "Mirko"

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    print(f1(N, points))

