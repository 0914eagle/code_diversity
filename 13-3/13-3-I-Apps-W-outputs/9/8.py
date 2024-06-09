
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(h, w, m, targets):
    # Initialize a 2D array to store the number of targets destroyed for each position
    destroyed = [[0] * w for _ in range(h)]

    # Loop through each target and update the number of targets destroyed for each position
    for target in targets:
        h_target, w_target = target
        destroyed[h_target - 1][w_target - 1] += 1
        destroyed[h_target - 1][:] = [max(destroyed[h_target - 1][i], destroyed[h_target - 1][i] + 1) for i in range(w)]
        destroyed[:][w_target - 1] = [max(destroyed[i][w_target - 1], destroyed[i][w_target - 1] + 1) for i in range(h)]

    # Return the maximum number of targets destroyed
    return max(max(row) for row in destroyed)

h, w, m = get_input()
targets = []
for _ in range(m):
    targets.append(get_input())

print(solve(h, w, m, targets))

