
def move_ball(moves):
    cups = [0, 0, 0]
    for move in moves:
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        elif move == "C":
            cups[0], cups[2] = cups[2], cups[0]
    return cups.index(1) + 1

def main():
    moves = input()
    print(move_ball(moves))

if __name__ == '__main__':
    main()

