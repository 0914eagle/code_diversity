
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
    
    # Fill in the targets for each column
    for i in range(n):
        for j in range(a[i]):
            # Find the next available row and column
            for k in range(n):
                if len(targets[k]) < 2:
                    targets[k].append([k+1, i+1])
                    break
    
    # Check if the configuration is valid
    if is_valid_configuration(n, a, targets):
        return targets
    else:
        return []

