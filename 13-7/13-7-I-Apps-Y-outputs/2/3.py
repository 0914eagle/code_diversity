
def solve(n):
    # Initialize a counter for the number of moves
    moves = 0
    
    # Loop until n is equal to 1 or 0
    while n != 1 and n != 0:
        # If n is divisible by 2, divide it by 2
        if n % 2 == 0:
            n //= 2
        # If n is divisible by 3, divide it by 3
        elif n % 3 == 0:
            n //= 3
        # If n is divisible by 5, divide it by 5
        elif n % 5 == 0:
            n //= 5
        # If n is not divisible by 2, 3, or 5, it is impossible to obtain 1
        else:
            return -1
        # Increment the move counter
        moves += 1
    
    # Return the number of moves required to obtain 1 from n
    return moves

