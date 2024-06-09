
def solve(arr):
    n = len(arr)
    neg_count = 0
    pos_count = 0
    for i in range(n):
        for j in range(i+1, n):
            product = 1
            for k in range(i, j+1):
                product *= arr[k]
            if product < 0:
                neg_count += 1
            elif product > 0:
                pos_count += 1
    return neg_count, pos_count

