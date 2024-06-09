
def solve(balls):
    # Initialize variables
    white_balls = []
    black_balls = []
    operations = 0

    # Separate the balls into white and black lists
    for ball in balls:
        if ball[1] == "W":
            white_balls.append(ball)
        else:
            black_balls.append(ball)

    # Sort the white and black lists
    white_balls.sort(key=lambda x: x[0])
    black_balls.sort(key=lambda x: x[0])

    # Iterate through the lists and count the number of swaps needed
    for i in range(len(white_balls)):
        if white_balls[i][0] != i + 1:
            operations += 1
    for i in range(len(black_balls)):
        if black_balls[i][0] != i + 1:
            operations += 1

    return operations

