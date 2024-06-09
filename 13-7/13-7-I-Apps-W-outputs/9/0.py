
def solve(a):
    n = len(a)
    neg_count, pos_count = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            prod = a[i]
            for k in range(i+1, j+1):
                prod *= a[k]
            if prod < 0:
                neg_count += 1
            elif prod > 0:
                pos_count += 1
    return neg_count, pos_count

