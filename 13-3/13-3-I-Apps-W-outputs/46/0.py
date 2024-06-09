
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, x, a):
    s = 0
    t = 0
    for i in range(n):
        s += 1 / (x ** a[i])
        t += a[i]
    gcd_st = gcd(s, t)
    return (s // gcd_st) % (10 ** 9 + 7)

