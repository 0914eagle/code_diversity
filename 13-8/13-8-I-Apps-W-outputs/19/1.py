
def solve(n, v, sellers):
    p = 0
    q = []
    for i, seller in enumerate(sellers, 1):
        for price in seller:
            if price <= v:
                p += 1
                q.append(i)
                break
    return p, q

