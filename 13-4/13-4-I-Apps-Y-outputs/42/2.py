
n = int(input())
a = list(map(int, input().split()))

result = [0] * (n + 1)
for i in range(2, n + 1):
    result[a[i]] += 1

for i in range(1, n + 1):
    print(result[i])

