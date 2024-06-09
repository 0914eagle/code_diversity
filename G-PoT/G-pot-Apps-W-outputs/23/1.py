
K = int(input())
ranks = list(map(int, input().split()))

ranks.sort(reverse=True)

min_declined = 0
for i in range(1, K+1):
    if ranks[i-1] != i:
        min_declined = i - 1
        break

print(min_declined)
