
n, m = map(int, input().split())

result = []
for i in range(1, n+1):
    result.append(2*i - 1)
    if 2*i <= m:
        result.append(2*i)

for num in result:
    print(num, end=' ')
