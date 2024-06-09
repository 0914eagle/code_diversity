
n, m, k = map(int, input().split())

antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

for i in range(1, 2**m):
    shops_to_visit = []
    for j in range(m):
        if i & (1 << j):
            shops_to_visit.append(j+1)
    
    if len(shops_to_visit) <= k:
        total_cost = 0
        for antique in antiques:
            if antique[0] in shops_to_visit:
                total_cost += antique[1]
            elif antique[2] in shops_to_visit:
                total_cost += antique[3]
        
        if len(set(shops_to_visit)) == k:
            min_cost = min(min_cost, total_cost)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
