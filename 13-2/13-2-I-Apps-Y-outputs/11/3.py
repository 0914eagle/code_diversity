
def solve(A, B):
    # Find the smallest common multiple of A and B
    scm = A * B // gcd(A, B)
    return scm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

