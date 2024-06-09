
def gcd(a, b, c):
    return __gcd(a, __gcd(b, c))

def __gcd(a, b):
    if b == 0:
        return a
    return __gcd(b, a % b)

def solve(K):
    result = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                result += gcd(a, b, c)
    return result

