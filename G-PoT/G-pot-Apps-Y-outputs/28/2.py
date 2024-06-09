
n, k = map(int, input().split())
ratings = list(map(int, input().split()))

indices = []
for i in range(n):
    if ratings[i] not in indices:
        indices.append(i+1)

if len(indices) < k:
    print("NO")
else:
    print("YES")
    print(*indices[:k])
