
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * (m + 1)
for i in range(n - 1):
    diff = (a[i + 1] - a[i]) % m
    count[diff] += 1

max_count = max(count)
result = sum(count) - max_count

print(result)
