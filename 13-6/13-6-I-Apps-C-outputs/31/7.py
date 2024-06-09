
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

    # Sort the white and black balls by their numbers
    white_balls.sort(key=lambda x: x[0])
    black_balls.sort(key=lambda x: x[0])

    # Check if the white and black balls are in the correct order
    for i in range(len(white_balls) - 1):
        if white_balls[i][0] > white_balls[i + 1][0]:
            operations += 1
        if black_balls[i][0] > black_balls[i + 1][0]:
            operations += 1

    return operations

