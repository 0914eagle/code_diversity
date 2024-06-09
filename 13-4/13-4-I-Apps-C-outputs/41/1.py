
def max_sum_after_k_swaps(arr, k):
    n = len(arr)
    def f(l, r):
        return sum(arr[l:r+1])
    def m():
        return max(f(i, j) for i in range(n) for j in range(i+1, n))
    for _ in range(k):
        max_sum = m()
        for i in range(n):
            for j in range(i+1, n):
                if f(i, j) == max_sum:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
    return m()

