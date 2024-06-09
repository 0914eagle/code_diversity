
def solve(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible values of k from 1 to 10
    for k in range(1, 11):
        # If a + k == b, we found the minimum number of moves
        if a + k == b:
            return 1
        # If a - k == b, we found the minimum number of moves
        if a - k == b:
            return 1
        # Otherwise, recurse with the updated value of a and the current minimum number of moves
        moves = solve(a + k, b)
        if moves < min_moves:
            min_moves = moves
        moves = solve(a - k, b)
        if moves < min_moves:
            min_moves = moves
    # Return the minimum number of moves
    return min_moves

