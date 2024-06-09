
def solve(queries):
    results = []
    for query in queries:
        n, k = map(int, query[0].split())
        prices = list(map(int, query[1].split()))
        max_price = max(prices)
        min_price = min(prices)
        if max_price - min_price <= 2 * k:
            results.append(max_price)
        else:
            results.append(-1)
    return results

