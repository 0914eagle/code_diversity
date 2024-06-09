
def f1(moves):
    # Initialize the cups and the ball
    cups = [0, 0, 0]
    ball = 1

    # Perform the moves
    for move in moves:
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]

    # Return the index of the cup with the ball
    return cups.index(1) + 1

def f2(moves):
    # Initialize the cups and the ball
    cups = [0, 0, 0]
    ball = 1

    # Perform the moves
    for move in moves:
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]

    # Return the index of the cup with the ball
    return cups.index(1) + 1

if __name__ == '__main__':
    moves = input()
    print(f1(moves))
    print(f2(moves))

