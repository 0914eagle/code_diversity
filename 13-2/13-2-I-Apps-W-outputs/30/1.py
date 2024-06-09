
def solve(a, b, c):
    result = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                result += i*j*k
    return result % 998244353

