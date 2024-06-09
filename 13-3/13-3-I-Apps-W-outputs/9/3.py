
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(H, W, M, targets):
    # Initialize a 2D array to store the number of targets destroyed for each cell
    destroyed = [[0] * W for _ in range(H)]

    # Loop through each target and mark the cells in the row and column as destroyed
    for i in range(M):
        h, w = targets[i]
        destroyed[h-1][w-1] = 1
        for j in range(H):
            destroyed[j][w-1] = 1
        for j in range(W):
            destroyed[h-1][j] = 1

    # Return the maximum number of targets destroyed
    return max(map(max, destroyed))

H, W, M = get_input()
targets = []
for i in range(M):
    h, w = get_input()
    targets.append((h, w))
print(solve(H, W, M, targets))

