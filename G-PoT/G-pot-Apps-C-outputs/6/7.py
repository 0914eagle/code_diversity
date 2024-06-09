
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * m
for i in range(n - 1):
    diff = (a[i + 1] - a[i] + m) % m
    count[a[i]] += diff
    count[a[i + 1]] -= diff

total = sum(abs(x) for x in count)
print(total // 2)
