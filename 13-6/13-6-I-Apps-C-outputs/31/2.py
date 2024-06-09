
def solve(balls):
    # Initialize variables
    num_balls = len(balls)
    num_operations = 0
    white_balls = [ball for ball in balls if ball[0] == 'W']
    black_balls = [ball for ball in balls if ball[0] == 'B']

    # Sort the white balls by their indices
    white_balls.sort(key=lambda x: x[1])

    # Sort the black balls by their indices
    black_balls.sort(key=lambda x: x[1])

    # Iterate through the white balls and black balls simultaneously
    # and check if they are in the correct position
    for i in range(num_balls):
        if white_balls[i][1] != i + 1:
            # If the white ball is not in the correct position,
            # swap it with the previous white ball
            white_balls[i], white_balls[i-1] = white_balls[i-1], white_balls[i]
            num_operations += 1
        if black_balls[i][1] != i + 1:
            # If the black ball is not in the correct position,
            # swap it with the previous black ball
            black_balls[i], black_balls[i-1] = black_balls[i-1], black_balls[i]
            num_operations += 1

    return num_operations

