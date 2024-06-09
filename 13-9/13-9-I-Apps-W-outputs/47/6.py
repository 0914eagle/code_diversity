
def solve(a):
    n = len(a)
    mod = 1000000007
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + a[i]) % mod
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = (suffix_sum[i + 1] + a[i]) % mod
    result = 0
    for i in range(n):
        result = (result + prefix_sum[i] * (i + 1) % mod) % mod
        result = (result + suffix_sum[i + 1] * (n - i) % mod) % mod
    return result

