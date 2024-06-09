
def solve(a, b):
    # Find the absolute difference between a and b
    diff = abs(a - b)

    # Initialize the minimum number of moves to 0
    min_moves = 0

    # While the absolute difference is greater than 0, we can perform moves
    while diff > 0:
        # If the absolute difference is odd, we can add 1 to make it even
        if diff % 2 == 1:
            diff += 1
        # If the absolute difference is even, we can subtract 2 to make it odd
        else:
            diff -= 2

        # Increment the minimum number of moves
        min_moves += 1

    # Return the minimum number of moves required to obtain b from a
    return min_moves

