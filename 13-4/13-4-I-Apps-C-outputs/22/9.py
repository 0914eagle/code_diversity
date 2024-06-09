
import math

def solve(N, salaries):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if salaries[i] > salaries[j]:
                expected_damages += salaries[i] - salaries[j]
    return expected_damages / (N ** 2)

N = int(input())
salaries = []
for i in range(N):
    L, R = map(float, input().split())
    salaries.append((L + R) / 2)

print(solve(N, salaries))

