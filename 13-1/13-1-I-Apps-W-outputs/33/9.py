
n, k, a, b, q = map(int, input().split())

orders = []

for i in range(q):
    query = input().split()
    if query[0] == "1":
        orders.append((int(query[1]), int(query[2])))
    else:
        p = int(query[1])
        filled_orders = 0
        for day, num_orders in orders:
            if day <= p:
                filled_orders += min(num_orders, b)
            elif day <= p + k - 1:
                filled_orders += 0
            else:
                filled_orders += min(num_orders, a)
        print(filled_orders)

