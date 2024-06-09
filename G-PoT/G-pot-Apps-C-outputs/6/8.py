
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * (m + 1)
for i in range(n - 1):
    diff = (a[i + 1] - a[i] + m) % m
    count[a[i]] += 1
    count[a[i + 1]] -= 1
    if diff != 1:
        count[1] += 1
        count[a[i + 1]] -= 1

total = sum(count)
result = total - max(count)
print(result)
