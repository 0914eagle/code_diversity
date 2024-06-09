
n = int(input())
durabilities = list(map(int, input().split()))

indices = list(range(1, n+1))
indices.sort(key=lambda i: durabilities[i-1] * (n-1) + 1)

total_shots = 0
for i in range(n):
    total_shots += durabilities[indices[i]-1] * i + 1

print(total_shots)
print(' '.join(map(str, indices)))
