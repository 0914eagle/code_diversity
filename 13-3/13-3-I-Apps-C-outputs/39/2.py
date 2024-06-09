
def f1(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Set the first point as the starting point
    board[1][1] = 1

    # Iterate through the points
    for i in range(2, N + 1):
        # Get the current point
        x, y = points[i - 1]

        # Check if the point is already taken
        if board[x][y] == 0:
            # Set the point as taken
            board[x][y] = 1

            # Check if the point is on the same row or column as the previous point
            if board[x - 1][y] == 1 or board[x][y - 1] == 1:
                # Set the previous point as the new starting point
                board[x - 1][y] = 2
            else:
                # Set the previous point as the new starting point
                board[x][y - 1] = 2
        else:
            # The point is already taken, so the game is over
            return "Slavko"

    # If the game ends without a winner, return "Mirko"
    return "Mirko"

def f2(...):
    # Implement the second function here
    pass

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    print(f1(N, points))

