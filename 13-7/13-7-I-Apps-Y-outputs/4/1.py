
def solve(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Loop through all possible values of x and y
    for x in range(1, a+1, 2):
        for y in range(1, a+1, 2):
            # Check if a+x or a-y is equal to b
            if a+x == b or a-y == b:
                # If it is, return the current number of moves
                return min_moves
            # If a+x or a-y is not equal to b, increment the number of moves
            min_moves += 1
    # If no value of x and y results in b, return the minimum number of moves
    return min_moves

