
def solve(l, r, k):
    result = 0
    for i in range(l, r+1):
        digits = set(str(i))
        if len(digits) <= k:
            result += i
    return result % 998244353

