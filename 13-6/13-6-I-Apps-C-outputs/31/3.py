
def solve(balls):
    # Initialize variables
    num_balls = len(balls)
    num_white_balls = num_balls // 2
    num_black_balls = num_white_balls
    white_balls = balls[:num_white_balls]
    black_balls = balls[num_white_balls:]
    operations = 0

    # Sort the white balls
    white_balls.sort(key=lambda x: x[1])

    # Sort the black balls
    black_balls.sort(key=lambda x: x[1])

    # Swap the white and black balls to achieve the objective
    for i in range(num_white_balls):
        if white_balls[i][1] != i + 1:
            operations += 1
            white_balls[i], white_balls[i + 1] = white_balls[i + 1], white_balls[i]

    for i in range(num_black_balls):
        if black_balls[i][1] != i + 1:
            operations += 1
            black_balls[i], black_balls[i + 1] = black_balls[i + 1], black_balls[i]

    return operations

