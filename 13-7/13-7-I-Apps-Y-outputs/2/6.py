
def get_min_moves(n):
    moves = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n = n // 3 * 2
        elif n % 5 == 0:
            n = n // 5 * 4
        else:
            return -1
        moves += 1
    return moves

