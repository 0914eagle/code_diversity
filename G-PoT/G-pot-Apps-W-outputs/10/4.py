
n, m = map(int, input().split())

order = []

for i in range(1, n+1):
    order.append(2*i - 1)
    order.append(2*i)

for i in range(1, m-2*n+1):
    order.append(4*n + i)

print(*order)
