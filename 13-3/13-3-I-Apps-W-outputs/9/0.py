
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(H, W, M, targets):
    # Initialize a 2D array to store the number of targets in each row and column
    rows = [0] * H
    cols = [0] * W

    # Loop through the targets and increment the number of targets in each row and column
    for i in range(M):
        row, col = targets[i]
        rows[row-1] += 1
        cols[col-1] += 1

    # Find the maximum number of targets that can be destroyed by placing the bomb in a row or column with the most targets
    max_targets = max(rows + cols)

    return max_targets

if __name__ == '__main__':
    H, W, M = get_input()
    targets = []
    for i in range(M):
        h, w = get_input()
        targets.append((h, w))
    print(solve(H, W, M, targets))

