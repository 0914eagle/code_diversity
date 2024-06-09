
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    H, W, M = get_input()
    targets = []
    for i in range(M):
        h, w = get_input()
        targets.append((h, w))
    
    # Initialize the maximum number of targets to destroy as 0
    max_targets = 0
    
    # Iterate over all possible positions for the bomb
    for h in range(1, H+1):
        for w in range(1, W+1):
            # Count the number of targets that can be destroyed at this position
            targets_destroyed = 0
            for target in targets:
                if target[0] == h or target[1] == w:
                    targets_destroyed += 1
            
            # Update the maximum number of targets to destroy if necessary
            if targets_destroyed > max_targets:
                max_targets = targets_destroyed
    
    return max_targets

if __name__ == '__main__':
    print(solve())

