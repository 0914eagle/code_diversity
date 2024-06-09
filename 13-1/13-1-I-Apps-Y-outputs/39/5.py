
def get_min_moves(a, b):
    moves = 0
    while a != b:
        if a > b:
            a -= 1
        else:
            a += 1
        moves += 1
    return moves

