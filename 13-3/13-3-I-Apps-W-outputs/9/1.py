
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    H, W, M = get_input()
    targets = []
    for i in range(M):
        h, w = get_input()
        targets.append((h, w))
    
    # Sort the targets by row and column
    targets.sort(key=lambda x: (x[0], x[1]))
    
    # Initialize the maximum number of targets to destroy
    max_targets = 0
    
    # Iterate through the targets and check if we can destroy them
    for i in range(M):
        # Get the current target
        h, w = targets[i]
        
        # Check if the target is in the same row or column as the previous target
        if i > 0 and targets[i-1][0] == h and targets[i-1][1] == w:
            # If the target is in the same row or column, we can't destroy it
            continue
        
        # Check if the target is in the same row or column as the next target
        if i < M-1 and targets[i+1][0] == h and targets[i+1][1] == w:
            # If the target is in the same row or column, we can't destroy it
            continue
        
        # If we reach here, we can destroy the target
        max_targets += 1
    
    return max_targets

print(solve())

