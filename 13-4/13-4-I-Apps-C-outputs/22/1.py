
import math

def solve(N, L, R):
    expected_payment = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] < L[j]:
                expected_payment += R[j] - R[i]
            elif L[i] > L[j]:
                expected_payment += R[i] - R[j]
            else:
                expected_payment += max(R[i], R[j]) - min(R[i], R[j])
    return expected_payment / (N * N)

N = int(input())
L = []
R = []
for i in range(N):
    L_i, R_i = map(float, input().split())
    L.append(L_i)
    R.append(R_i)

print(solve(N, L, R))

