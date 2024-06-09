
def is_valid_configuration(n, a, targets):
    # Check if the targets are valid
    for i in range(n):
        if len(targets[i]) > 2:
            return False
    
    # Check if the targets are unique
    for i in range(n):
        for j in range(i+1, n):
            if targets[i] == targets[j]:
                return False
    
    # Check if the targets are in the correct rows and columns
    for i in range(n):
        for target in targets[i]:
            if target[0] != i+1 and target[1] != i+1:
                return False
    
    # Check if the number of targets matches the number of hits
    for i in range(n):
        if len(targets[i]) != a[i]:
            return False
    
    return True

def solve(n, a):
    # Initialize the targets as empty lists
    targets = [[] for _ in range(n)]
    
    # Fill in the targets row by row
    for i in range(n):
        # Check if the current row has enough space for the targets
        if len(targets[i]) == 2:
            return -1
        
        # Add the targets to the current row
        for j in range(a[i]):
            targets[i].append([i+1, j+1])
    
    # Check if the configuration is valid
    if is_valid_configuration(n, a, targets):
        return targets
    else:
        return -1

