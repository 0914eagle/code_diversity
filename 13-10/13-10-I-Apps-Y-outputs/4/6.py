
def move_cups(moves):
    # Initialize the cups with the ball under the leftmost cup
    cups = [0, 0, 0]
    cups[0] = 1

    # Perform the moves
    for move in moves:
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        elif move == "C":
            cups[0], cups[2] = cups[2], cups[0]

    # Return the index of the cup with the ball
    return cups.index(1)

def main():
    moves = input()
    print(move_cups(moves))

if __name__ == '__main__':
    main()

