
N, K, X, Y = map(int, input().split())

total = 0
for i in range(1, N+1):
    if i <= K:
        total += X
    else:
        total += Y

print(total)

