
def climb_stairs(n, m):
    # Initialize a list to store the number of moves for each step
    moves = [0] * (n + 1)
    # Initialize a list to store the number of moves for each step that is a multiple of m
    multiples = [0] * (n + 1)
    
    # Base case: when we reach the top of the stairs
    moves[n] = 1
    multiples[n] = 1
    
    # Iterate through the stairs
    for step in range(n - 1, 0, -1):
        # There are two ways to climb each step: 1 step and 2 steps
        moves[step] = moves[step + 1] + moves[step + 2]
        # If the number of moves is a multiple of m, add it to the list of multiples
        if moves[step] % m == 0:
            multiples[step] = 1
    
    # Return the minimum number of moves that is a multiple of m
    return min(moves[1::m])

