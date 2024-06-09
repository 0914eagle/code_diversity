
# Read input
n, m, k = map(int, input().split())
antiques = []
for _ in range(n):
    a, p, b, q = map(int, input().split())
    antiques.append((a, p, b, q))

# Initialize minimum cost to a large value
min_cost = float('inf')

# Try all combinations of k shops
for shops in range(1, 1 << m):
    if bin(shops).count('1') == k:
        total_cost = 0
        bought = set()
        for a, p, b, q in antiques:
            min_price = float('inf')
            for i in range(m):
                if shops & (1 << i):
                    if i + 1 == a:
                        min_price = min(min_price, p)
                    elif i + 1 == b:
                        min_price = min(min_price, q)
            if min_price == float('inf'):
                total_cost = -1
                break
            total_cost += min_price
        if total_cost != -1:
            min_cost = min(min_cost, total_cost)

# Output the result
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
