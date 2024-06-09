
def solve(a):
    n = len(a)
    neg_count = 0
    pos_count = 0
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j+1):
                product *= a[k]
            if product < 0:
                neg_count += 1
            elif product > 0:
                pos_count += 1
    return neg_count, pos_count

