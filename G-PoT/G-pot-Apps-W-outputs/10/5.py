
n, m = map(int, input().split())

result = []
for i in range(1, n+1):
    if m >= 2*i:
        result.extend([2*i-1, 2*i])

if m > 2*n:
    for i in range(2*n+1, m+1):
        result.append(i)

print(*result)
