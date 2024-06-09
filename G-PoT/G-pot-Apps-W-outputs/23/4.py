
K = int(input())
ranks = list(map(int, input().split()))

ranks.sort()

min_declined = 0
for i in range(K):
    if ranks[i] > i + 1:
        min_declined += ranks[i] - (i + 1)

print(min_declined)
