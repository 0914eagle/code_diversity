
def solve(n, hits):
    # Initialize a 2D array to store the configuration of targets
    targets = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Populate the array with the given number of hits for each column
    for i in range(1, n + 1):
        targets[n][i] = hits[i - 1]
    
    # Check if the configuration is valid
    if not is_valid(targets):
        return -1
    
    # If the configuration is valid, return the number of targets and their positions
    t = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if targets[i][j] == 1:
                t += 1
                print(i, j)
    
    return t

def is_valid(targets):
    # Check if each row has at most 2 targets
    for i in range(1, len(targets)):
        if len([j for j in range(1, len(targets[0])) if targets[i][j] == 1]) > 2:
            return False
    
    # Check if each column has at most 2 targets
    for j in range(1, len(targets[0])):
        if len([i for i in range(1, len(targets)) if targets[i][j] == 1]) > 2:
            return False
    
    return True

