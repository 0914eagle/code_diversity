
def solve(n, v, prices):
    sellers = []
    for i, seller in enumerate(prices, 1):
        for price in seller:
            if price <= v:
                sellers.append(i)
                break
    return len(sellers), *sellers

