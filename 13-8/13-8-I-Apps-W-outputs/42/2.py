
def f(r, c):
    if r == 0 or c == 0:
        return 1
    elif r == 1 and c == 1:
        return 2
    else:
        return (f(r-1, c) + f(r, c-1)) % 1000000007

def solve(r1, c1, r2, c2):
    return sum(f(i, j) for i in range(r1, r2+1) for j in range(c1, c2+1)) % 1000000007

