
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * (m + 1)
for i in range(n - 1):
    diff = (a[i + 1] - a[i] + m) % m
    count[a[i]] += 1
    count[a[i + 1]] -= 1
    if diff > 0:
        if a[i + 1] > a[i]:
            count[1] += 1
            count[a[i] + 1] -= 1
        else:
            count[a[i] + 1] += 1
            count[1] -= 1

ans = float('inf')
cur = 0
for i in range(1, m + 1):
    cur += count[i]
    ans = min(ans, cur)

print(ans)
