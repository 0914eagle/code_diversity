
K = int(input())
ranks = list(map(int, input().split()))

ranks.sort()
missing_contestants = 0
for i in range(1, K+1):
    if ranks[i-1] != i:
        missing_contestants += ranks[i-1] - i

print(missing_contestants)
