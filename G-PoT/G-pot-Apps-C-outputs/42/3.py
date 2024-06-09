
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

min_cost = float('inf')

def backtrack(curr_shop, visited, total_cost):
    nonlocal min_cost
    if len(visited) == n:
        min_cost = min(min_cost, total_cost)
        return
    if len(visited) + m - curr_shop < n:
        return
    if len(visited) + m - curr_shop > k:
        return
    for i in range(curr_shop, m):
        for a, p, b, q in antiques:
            if i == a - 1:
                backtrack(i + 1, visited + [a], total_cost + p)
            elif i == b - 1:
                backtrack(i + 1, visited + [b], total_cost + q)

backtrack(0, [], 0)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
