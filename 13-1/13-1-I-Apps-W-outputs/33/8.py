
import sys

n, k, a, b, q = map(int, input().split())

orders = [0] * (n + 1)

for i in range(q):
    query = input().split()
    if query[0] == "1":
        d, a = map(int, query[1:])
        orders[d] += a
    else:
        p = int(query[1])
        filled_orders = 0
        for j in range(p, n + 1):
            filled_orders += min(orders[j], b)
        print(filled_orders)


