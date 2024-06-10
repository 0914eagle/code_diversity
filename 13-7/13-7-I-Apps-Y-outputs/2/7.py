
def is_divisible_by_25(n):
    while n % 25 != 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def get_min_moves(n):
    if is_divisible_by_25(n):
        return 0
    
    moves = 0
    while not is_divisible_by_25(n):
        if n % 10 == 0:
            return -1
        n //= 10
        moves += 1
    
    return moves

if __name__ == '__main__':
    n = int(input())
    print(get_min_moves(n))

