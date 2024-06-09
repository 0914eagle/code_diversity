
n, m = map(int, input().split())
a = list(map(int, input().split()))

diffs = []
for i in range(n - 1):
    diff = abs(a[i] - a[i + 1])
    if diff != 0:
        diffs.append(diff)

diffs.sort()

total_diff = sum(diffs)
max_diff = max(diffs)

result = total_diff - max_diff
print(result)
