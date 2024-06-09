
def f1(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the previous point
    current_player = "Mirko"
    previous_point = (0, 0)

    # Iterate through the points
    for i in range(N):
        # Get the current point
        current_point = points[i]

        # Check if the current player can play
        if board[current_point[0]][current_point[1]] == 0:
            # Update the game board
            board[current_point[0]][current_point[1]] = 1

            # Update the previous point
            previous_point = current_point

            # Switch the current player
            if current_player == "Mirko":
                current_player = "Slavko"
            else:
                current_player = "Mirko"
        else:
            # The current player cannot play, so the game is over
            break

    # Check if Mirko has a winning strategy
    if current_player == "Mirko":
        return "Mirko"
    else:
        return "Slavko"

def f2(N, points):
    # Initialize the game board
    board = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the current player and the previous point
    current_player = "Slavko"
    previous_point = (0, 0)

    # Iterate through the points
    for i in range(N):
        # Get the current point
        current_point = points[i]

        # Check if the current player can play
        if board[current_point[0]][current_point[1]] == 0:
            # Update the game board
            board[current_point[0]][current_point[1]] = 1

            # Update the previous point
            previous_point = current_point

            # Switch the current player
            if current_player == "Slavko":
                current_player = "Mirko"
            else:
                current_player = "Slavko"
        else:
            # The current player cannot play, so the game is over
            break

    # Check if Slavko has a winning strategy
    if current_player == "Slavko":
        return "Slavko"
    else:
        return "Mirko"

if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    print(f1(N, points))

