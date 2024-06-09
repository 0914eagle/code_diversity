
K = int(input())
ranks = list(map(int, input().split()))

ranks.sort()
min_declined = 0

for i in range(1, K+1):
    if ranks[i-1] != i:
        min_declined = max(min_declined, i - ranks[i-1])

print(min_declined)
