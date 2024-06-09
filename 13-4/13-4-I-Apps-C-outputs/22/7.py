
import math

def solve(N, LR_pairs):
    expected_damages = 0
    for i in range(N):
        L, R = LR_pairs[i]
        damages = 0
        for j in range(i+1, N):
            L_j, R_j = LR_pairs[j]
            if L_j > L:
                damages += R_j - L
            if R_j < R:
                damages += R - R_j
        expected_damages += damages / (N - i - 1)
    return expected_damages / N ** 2

N = int(input())
LR_pairs = []
for i in range(N):
    L, R = map(float, input().split())
    LR_pairs.append((L, R))

print(solve(N, LR_pairs))

