
n, m = map(int, input().split())
a = list(map(int, input().split()))

diff = [0] * n
for i in range(n - 1):
    diff[i] = (a[i+1] - a[i] + m) % m

total_diff = sum(diff)
max_diff = max(diff)

result = total_diff - max_diff
print(result)
