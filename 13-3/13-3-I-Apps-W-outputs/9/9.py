
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(H, W, M, targets):
    # Initialize a 2D array to store the number of targets destroyed in each row and column
    destroyed = [[0] * W for _ in range(H)]

    # Loop through the targets and update the number of targets destroyed in each row and column
    for target in targets:
        h, w = target
        destroyed[h-1][w-1] += 1
        destroyed[h-1][w-1] += 1

    # Find the maximum number of targets destroyed by placing the bomb in a row or column with the most targets destroyed
    max_destroyed = 0
    for row in destroyed:
        max_destroyed = max(max_destroyed, max(row))

    return max_destroyed

if __name__ == '__main__':
    H, W, M = get_input()
    targets = []
    for _ in range(M):
        h, w = get_input()
        targets.append((h, w))

    print(solve(H, W, M, targets))

