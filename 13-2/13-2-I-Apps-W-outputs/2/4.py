
def solve(n, k):
    for x in range(n):
        if sum(int(d) for d in str(x)) + sum(int(d) for d in str(x + 1)) + ... + sum(int(d) for d in str(x + k)) == n:
            return x
    return -1

