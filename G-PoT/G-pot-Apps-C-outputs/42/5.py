
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

for i in range(1, 2**m):
    shops_to_visit = [j for j in range(1, m+1) if (i >> (j-1)) & 1]
    if len(shops_to_visit) <= k:
        total_cost = 0
        for antique in antiques:
            cost_original = antique[1] if antique[0] in shops_to_visit else float('inf')
            cost_knockoff = antique[3] if antique[2] in shops_to_visit else float('inf')
            total_cost += min(cost_original, cost_knockoff)
        min_cost = min(min_cost, total_cost)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
