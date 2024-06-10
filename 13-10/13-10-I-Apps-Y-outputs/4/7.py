
def determine_cup(moves):
    # Initialize the cups and the ball
    cups = [False, False, False]
    ball = 0
    
    # Perform the moves
    for move in moves:
        if move == 'A':
            cups[0], cups[1] = cups[1], cups[0]
        elif move == 'B':
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]
    
    # Find the cup with the ball
    for i in range(len(cups)):
        if cups[i]:
            ball = i + 1
            break
    
    return ball

def main():
    moves = input()
    print(determine_cup(moves))

if __name__ == '__main__':
    main()

