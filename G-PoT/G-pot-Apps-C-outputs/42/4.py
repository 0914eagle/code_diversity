
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

def backtrack(cost, visited, shop_count):
    nonlocal min_cost
    if len(visited) == n:
        min_cost = min(min_cost, cost)
        return
    if shop_count == k:
        return
    for i in range(n):
        if i not in visited:
            a, p, b, q = antiques[i]
            if a not in visited:
                backtrack(cost + p, visited | {a}, shop_count + 1)
            if b not in visited:
                backtrack(cost + q, visited | {b}, shop_count + 1)

backtrack(0, set(), 0)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
