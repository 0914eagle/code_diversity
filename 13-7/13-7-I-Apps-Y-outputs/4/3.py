
def get_min_moves(a, b):
    # Calculate the absolute difference between a and b
    diff = abs(a - b)

    # Initialize the minimum number of moves to 0
    min_moves = 0

    # Loop until the difference is 0
    while diff > 0:
        # If the difference is odd, add 1 to the minimum number of moves
        if diff % 2 == 1:
            min_moves += 1

        # Divide the difference by 2
        diff //= 2

    # Return the minimum number of moves
    return min_moves

