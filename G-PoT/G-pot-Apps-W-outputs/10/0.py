
n, m = map(int, input().split())

result = []

for i in range(1, n+1):
    if m >= 2*i:
        result.append(2*i-1)
    if m >= 2*i-1:
        result.append(2*i)

for i in range(1, n+1):
    if m > 2*n:
        if m >= 2*n+i:
            result.append(2*n+i)
        if m >= 3*n+i:
            result.append(3*n+i)

print(*result)
