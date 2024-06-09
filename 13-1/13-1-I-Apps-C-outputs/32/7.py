
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
            row = 0
            column = 0
            while True:
                if targets[column]:
                    row = targets[column][-1][0] + 1
                if row > n:
                    return -1
                if row not in [target[0] for target in targets[column]]:
                    break
                column += 1
            targets[column].append((row, i+1))
    
    # Check if the configuration is valid
    if is_valid_configuration(n, a, targets):
        return targets
    else:
        return -1

