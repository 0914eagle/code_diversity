
def solve(balls):
    # Initialize variables
    num_white = 0
    num_black = 0
    white_balls = []
    black_balls = []
    operations = 0

    # Separate the balls into white and black lists
    for ball in balls:
        if ball[0] == "W":
            white_balls.append(ball[1])
            num_white += 1
        else:
            black_balls.append(ball[1])
            num_black += 1

    # Sort the white and black lists
    white_balls.sort()
    black_balls.sort()

    # Check if the lists are already in order
    if white_balls == list(range(1, num_white + 1)) and black_balls == list(range(1, num_black + 1)):
        return operations

    # Swap the first white and black balls
    white_balls[0], black_balls[0] = black_balls[0], white_balls[0]
    operations += 1

    # Check if the lists are now in order
    if white_balls == list(range(1, num_white + 1)) and black_balls == list(range(1, num_black + 1)):
        return operations

    # Swap the last white and black balls
    white_balls[-1], black_balls[-1] = black_balls[-1], white_balls[-1]
    operations += 1

    # Check if the lists are now in order
    if white_balls == list(range(1, num_white + 1)) and black_balls == list(range(1, num_black + 1)):
        return operations

    # Swap the first white and last white balls
    white_balls[0], white_balls[-1] = white_balls[-1], white_balls[0]
    operations += 1

    # Check if the lists are now in order
    if white_balls == list(range(1, num_white + 1)) and black_balls == list(range(1, num_black + 1)):
        return operations

    # Swap the first black and last black balls
    black_balls[0], black_balls[-1] = black_balls[-1], black_balls[0]
    operations += 1

    # Check if the lists are now in order
    if white_balls == list(range(1, num_white + 1)) and black_balls == list(range(1, num_black + 1)):
        return operations

    # If the lists are not in order, return -1
    return -1

