
def get_min_moves(n, m):
    # Initialize a list to store the number of moves for each step
    moves = [0] * (n + 1)
    # Initialize a list to store the number of moves for each step that is a multiple of m
    multiples = [0] * (n + 1)
    
    # Base case: when n is 0, there is 1 way to climb 0 steps
    moves[0] = 1
    multiples[0] = 1
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # There are two ways to climb i steps: 1 step + i - 1 steps or 2 steps + i - 2 steps
        moves[i] = moves[i - 1] + moves[i - 2]
        # If the number of moves is a multiple of m, add it to the list of multiples
        if moves[i] % m == 0:
            multiples[i] = moves[i]
    
    # Return the last element of the list of multiples, which is the minimal number of moves that is a multiple of m
    return multiples[-1]

