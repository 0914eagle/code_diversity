
def solve(n, a):
    # Check if the number of targets is valid
    if sum(a) % 2 != 0:
        return -1
    
    # Initialize the targets dictionary
    targets = {}
    for i in range(n):
        targets[i+1] = []
    
    # Populate the targets dictionary
    for i in range(n):
        for j in range(a[i]):
            targets[i+1].append((i+1, j+1))
    
    # Check if the targets are valid
    for i in range(n):
        if len(targets[i+1]) > 2:
            return -1
    
    # Return the targets configuration
    return targets

