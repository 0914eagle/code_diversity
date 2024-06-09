
def solve(a):
    n = len(a)
    neg_prod = 0
    pos_prod = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= a[j]
            if prod < 0:
                neg_prod += 1
            elif prod > 0:
                pos_prod += 1
    return neg_prod, pos_prod

