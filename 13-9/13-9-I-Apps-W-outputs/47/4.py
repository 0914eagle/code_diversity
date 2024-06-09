
def solve(arr):
    n = len(arr)
    sum_f = 0
    for l in range(n):
        for r in range(l, n):
            b = arr[l:r+1]
            b.sort()
            sum_f += sum(b[i] * (i + 1) for i in range(len(b)))
    return sum_f % (10**9 + 7)

