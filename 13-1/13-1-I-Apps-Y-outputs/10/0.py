
def f1(n):
    # Initialize variables
    moves = 0
    while n % 25 != 0:
        # Check if the last digit is 0
        if n % 10 == 0:
            return -1
        # Swap the last two digits
        n = n // 10 + n % 10 * 10
        moves += 1
    return moves

