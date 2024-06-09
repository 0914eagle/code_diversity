
def solve(n, s):
    for b in range(2, 10**11+1):
        if f(b, n) == s:
            return b
    return -1

def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n//b) + (n%b)

