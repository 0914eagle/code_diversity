
def solve(balls):
    # Initialize variables
    num_balls = len(balls)
    num_white_balls = num_balls // 2
    num_black_balls = num_balls // 2
    white_balls = balls[:num_white_balls]
    black_balls = balls[num_white_balls:]
    operations = 0

    # Sort the white balls
    white_balls.sort(key=lambda x: x[1])

    # Sort the black balls
    black_balls.sort(key=lambda x: x[1])

    # Swap the first white ball with the first black ball if necessary
    if white_balls[0][1] > black_balls[0][1]:
        operations += 1
        white_balls[0], black_balls[0] = black_balls[0], white_balls[0]

    # Swap the last white ball with the last black ball if necessary
    if white_balls[-1][1] < black_balls[-1][1]:
        operations += 1
        white_balls[-1], black_balls[-1] = black_balls[-1], white_balls[-1]

    return operations

