
import sys

def solve(n, engineers):
    # Calculate the number of possible assignments
    num_assignments = 1
    for engineer in engineers:
        num_assignments *= (n - 1)
    return num_assignments % 1000000007

n = int(input())
engineers = []
for i in range(n):
    current_desk, desired_desk = map(int, input().split())
    engineers.append((current_desk, desired_desk))

print(solve(n, engineers))

