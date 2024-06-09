
def solve(v, n, prices):
    sellers = []
    for i in range(n):
        for j in range(len(prices[i])):
            if prices[i][j] <= v:
                sellers.append(i)
                break
    return len(sellers), sorted(sellers)

