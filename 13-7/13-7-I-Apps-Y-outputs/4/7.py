
def solve(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible odd numbers x
    for x in range(1, a + 1, 2):
        # If a + x equals b, we found the minimum number of moves
        if a + x == b:
            return 1
        # If a + x is greater than b, we can't obtain b from a in this move
        elif a + x > b:
            continue
        # Otherwise, recursively call the function to find the minimum number of moves to obtain b from a + x
        min_moves = min(min_moves, solve(a + x, b))
    # Loop through all possible even numbers y
    for y in range(2, a + 1, 2):
        # If a - y equals b, we found the minimum number of moves
        if a - y == b:
            return 1
        # If a - y is less than b, we can't obtain b from a in this move
        elif a - y < b:
            continue
        # Otherwise, recursively call the function to find the minimum number of moves to obtain b from a - y
        min_moves = min(min_moves, solve(a - y, b))
    # Return the minimum number of moves
    return min_moves + 1

