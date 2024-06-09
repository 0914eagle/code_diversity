
n, m = map(int, input().split())

order = []
for i in range(1, n+1):
    order.append(2*i - 1)
    order.append(2*i)

for i in range(1, m+1):
    print(order[(i-1) % (2*n)], end=' ')
