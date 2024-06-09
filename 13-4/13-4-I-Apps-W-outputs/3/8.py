
n = int(input())
guard_prices = []
for i in range(4):
    a, b, c, d = map(int, input().split())
    guard_prices.append([[a, b], [c, d]])

# Find the guardpost with the minimum total price
min_total_price = float('inf')
min_guardpost = -1
for i in range(4):
    total_price = guard_prices[i][0][0] + guard_prices[i][1][0]
    if total_price <= n and total_price < min_total_price:
        min_total_price = total_price
        min_guardpost = i + 1

if min_guardpost == -1:
    print(-1)
else:
    print(min_guardpost, guard_prices[min_guardpost - 1][0][0], guard_prices[min_guardpost - 1][1][0])

