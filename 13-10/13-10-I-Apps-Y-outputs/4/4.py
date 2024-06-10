
def get_ball_position(moves):
    # Initialize the position of the ball as the left cup
    ball_position = 1

    # Iterate through each move
    for move in moves:
        # If the move is "A", swap the left and middle cups
        if move == "A":
            ball_position = 2 if ball_position == 1 else 1
        # If the move is "B", swap the middle and right cups
        elif move == "B":
            ball_position = 3 if ball_position == 2 else 2
        # If the move is "C", swap the left and right cups
        elif move == "C":
            ball_position = 1 if ball_position == 3 else 3

    # Return the position of the ball
    return ball_position

def main():
    moves = input()
    ball_position = get_ball_position(moves)
    print(ball_position)

if __name__ == '__main__':
    main()

