
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
    
    # Initialize the maximum number of targets to destroy to 0
    max_targets = 0
    
    # Iterate through the targets and check if they are in the same row or column as the previous target
    for i in range(M):
        if i == 0:
            max_targets += 1
        else:
            current_target = targets[i]
            previous_target = targets[i-1]
            if current_target[0] == previous_target[0] or current_target[1] == previous_target[1]:
                max_targets += 1
    
    return max_targets

print(solve())

