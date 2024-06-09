
n, m = map(int, input().split())

result = []
for i in range(1, n+1):
    if m >= 2:
        result.append(2*i - 1)
        result.append(2*i)
        m -= 2
    else:
        result.append(2*i - 1)
        m -= 1
    if m == 0:
        break

print(*result)
