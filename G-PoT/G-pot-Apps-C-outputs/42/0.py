
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

for shops in range(1, 1 << m):
    if bin(shops).count('1') <= k:
        cost = 0
        bought = set()
        for a, p, b, q in antiques:
            if shops & (1 << (a-1)):
                cost += p
                bought.add(a)
            elif shops & (1 << (b-1)):
                cost += q
                bought.add(b)
        if len(bought) == n:
            min_cost = min(min_cost, cost)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
