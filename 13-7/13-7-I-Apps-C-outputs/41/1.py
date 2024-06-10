
def get_shortcuts(k):
    shortcuts = {}
    shortcuts['R'] = 'SrS'
    shortcuts['S'] = 'rr'
    shortcuts['I'] = 'lldll'
    return shortcuts

def get_moves(k, organs, empty_space):
    moves = []
    for i in range(1, 4*k+1):
        if organs[i] != i:
            moves.append(organs[i])
    moves.append(empty_space)
    return moves

def get_sequence_of_moves(k, organs, empty_space):
    moves = get_moves(k, organs, empty_space)
    sequence_of_moves = ''
    for move in moves:
        if move == empty_space:
            sequence_of_moves += 'E'
        else:
            sequence_of_moves += move
    return sequence_of_moves

def main():
    t = int(input())
    for i in range(t):
        k = int(input())
        organs = [int(x) for x in input().split()]
        empty_space = input()
        shortcuts = get_shortcuts(k)
        sequence_of_moves = get_sequence_of_moves(k, organs, empty_space)
        print('SURGERY COMPLETE')
        for shortcut, move in shortcuts.items():
            print(shortcut, move)
        print(sequence_of_moves)
        print('DONE')

if __name__ == '__main__':
    main()

