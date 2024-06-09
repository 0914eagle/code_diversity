
def solve(balls):
    # Initialize variables
    white_balls = []
    black_balls = []
    operations = 0

    # Separate the white and black balls
    for ball in balls:
        if ball[1] == "W":
            white_balls.append(ball)
        else:
            black_balls.append(ball)

    # Sort the white balls in ascending order
    white_balls.sort(key=lambda x: x[0])

    # Sort the black balls in ascending order
    black_balls.sort(key=lambda x: x[0])

    # Swap the first white ball with the first black ball
    operations += 1
    white_balls[0], black_balls[0] = black_balls[0], white_balls[0]

    # Swap the last white ball with the last black ball
    operations += 1
    white_balls[-1], black_balls[-1] = black_balls[-1], white_balls[-1]

    return operations

