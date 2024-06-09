
n, m = map(int, input().split())
a = list(map(int, input().split()))

diffs = []
for i in range(n-1):
    diff = (a[i+1] - a[i] + m) % m
    diffs.append(diff)

total_diff = sum(diffs)
max_diff = max(diffs)

result = total_diff - max_diff
print(result)
