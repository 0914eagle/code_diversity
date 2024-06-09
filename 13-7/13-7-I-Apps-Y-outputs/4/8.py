
def solve(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible odd numbers x
    for x in range(1, a + 1, 2):
        # If a + x equals b, we found the minimum number of moves
        if a + x == b:
            return 1
        # If a + x is greater than b, we can't obtain b from a in one move
        elif a + x > b:
            continue
        # Loop through all possible even numbers y
        for y in range(2, a + 1, 2):
            # If a - y equals b, we found the minimum number of moves
            if a - y == b:
                return 1
            # If a - y is greater than b, we can't obtain b from a in one move
            elif a - y > b:
                continue
            # If a + x and a - y are both less than or equal to b, we can obtain b from a in two moves
            if a + x <= b and a - y <= b:
                min_moves = min(min_moves, 2)
    # If the minimum number of moves is infinity, it means we can't obtain b from a in any number of moves
    if min_moves == float('inf'):
        return -1
    # Return the minimum number of moves
    return min_moves

