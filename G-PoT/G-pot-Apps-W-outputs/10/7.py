
n, m = map(int, input().split())

order = []
for i in range(1, n+1):
    order.append(2*i - 1)
    order.append(2*i)

for i in range(n+1, m+1):
    order.append(i)

print(*order)
