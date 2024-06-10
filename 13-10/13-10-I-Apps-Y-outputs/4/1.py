
def check_cup_position(moves):
    # Initialize the cup positions
    cups = [False, False, False]

    # Iterate through each move
    for move in moves:
        # Check if the move is valid
        if move not in ["A", "B", "C"]:
            return -1

        # Update the cup positions
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]

    # Return the index of the cup under which the ball is
    return cups.index(True) + 1

def main():
    # Get the moves from the input
    moves = input()

    # Call the check_cup_position function and print the result
    print(check_cup_position(moves))

if __name__ == '__main__':
    main()

