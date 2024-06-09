
def solve(n, a):
    # Check if the number of targets is valid
    if sum(a) > 2 * n:
        return -1
    
    # Initialize the target configuration
    targets = []
    for i in range(n):
        targets.append([])
    
    # Place the targets
    for i in range(n):
        # Check if the target is already placed
        if len(targets[i]) == 2:
            continue
        
        # Place the target
        targets[i].append(a[i])
        
        # Update the number of targets
        a[i] -= 1
    
    # Check if all targets are placed
    if sum(a) > 0:
        return -1
    
    # Return the target configuration
    return targets

