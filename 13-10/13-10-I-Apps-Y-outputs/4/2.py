
def get_cups_states(moves):
    states = []
    for move in moves:
        if move == "A":
            states.append([True, False, False])
        elif move == "B":
            states.append([False, True, False])
        else:
            states.append([False, False, True])
    return states

def get_ball_cup(states):
    for state in states:
        if state[0]:
            return 1
        if state[1]:
            return 2
        if state[2]:
            return 3
    return -1

def main():
    moves = input()
    states = get_cups_states(moves)
    ball_cup = get_ball_cup(states)
    print(ball_cup)

if __name__ == '__main__':
    main()

