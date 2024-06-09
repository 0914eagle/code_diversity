
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(H, W, M, targets):
    # Initialize a 2D array to store the number of targets destroyed for each position
    destroyed = [[0] * W for _ in range(H)]

    # Loop through each target and increment the number of targets destroyed for each position
    for target in targets:
        h, w = target
        destroyed[h-1][w-1] += 1
        destroyed[h-1][w] += 1
        destroyed[h][w-1] += 1
        destroyed[h][w] += 1

    # Find the maximum number of targets destroyed
    max_destroyed = 0
    for row in destroyed:
        for num in row:
            max_destroyed = max(max_destroyed, num)

    return max_destroyed

def main():
    H, W, M = get_input()
    targets = []
    for _ in range(M):
        targets.append(get_input())
    print(solve(H, W, M, targets))

if __name__ == "__main__":
    main()

