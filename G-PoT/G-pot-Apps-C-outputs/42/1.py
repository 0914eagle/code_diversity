
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

for shops in range(1, 1 << m):
    if bin(shops).count('1') <= k:
        cost = 0
        visited_shops = set()
        for a, p, b, q in antiques:
            if shops & (1 << (a - 1)):
                cost += p
                visited_shops.add(a)
            else:
                cost += q
                visited_shops.add(b)
        if len(visited_shops) <= k:
            min_cost = min(min_cost, cost)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
