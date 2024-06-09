
def solve(arr):
    n = len(arr)
    sum_f = 0
    for i in range(n):
        for j in range(i, n):
            sum_f += arr[j] * (j - i + 1)
    return sum_f % 1000000007

