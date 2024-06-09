
import math
import cmath

def f(x):
    return c * math.gamma(x) + cmath.sqrt(math.log(math.erf(t3 * x))) - math.jn(k, x) ** t4

def p(x, n):
    return sum([f(i) * x**i / math.factorial(i) for i in range(n+1)])

def p_n(x, n):
    return sum([p(i, n-1) * x**i for i in range(n)])

def g(x, n):
    return p_n(x, n).derivative()

def location(n, k, r, s, l):
    x = g(n, r+s).derivative() + l
    return round(x, 2)

a, b, c = map(float, input().split())
t1, t2, t3, t4 = map(int, input().split())
n, k, r, s, l = map(int, input().split())

print(location(n, k, r, s, l))

