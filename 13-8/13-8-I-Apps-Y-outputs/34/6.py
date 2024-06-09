
def solve(x):
    k = 0
    for i in range(1, x):
        if x % i == 0 and i > k:
            k = i
    return k

