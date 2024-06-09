
def solve(A, B):
    # Find the smallest common multiple of A and B
    scm = A * B // gcd(A, B)
    return scm

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

