
def get_moves(moves_string):
    return moves_string.split()

def get_ball_position(moves):
    start_position = 1
    for move in moves:
        if move == "A":
            start_position = 2
        elif move == "B":
            start_position = 3
        elif move == "C":
            start_position = 1
    return start_position

def main():
    moves = get_moves(input())
    ball_position = get_ball_position(moves)
    print(ball_position)

if __name__ == '__main__':
    main()

