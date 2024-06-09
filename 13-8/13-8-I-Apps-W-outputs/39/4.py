
def solve(n, m, k, b):
    # Calculate the number of distinct strings modulo 998244353
    result = 1
    for i in range(m):
        result = result * (k - b[i] + 1) % 998244353
    return result

