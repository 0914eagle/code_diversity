
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

for i in range(1, m+1):
    for j in range(1, m+1):
        if i == j:
            continue
        visited_shops = set([i, j])
        total_cost = 0
        for a, p, b, q in antiques:
            if a in visited_shops and b in visited_shops:
                total_cost += min(p, q)
        if len(visited_shops) <= k:
            min_cost = min(min_cost, total_cost)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
