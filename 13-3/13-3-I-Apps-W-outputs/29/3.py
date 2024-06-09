
def solve(n, a):
    # Calculate the minimum number of seconds it will take to pick up all the prizes
    return sum(abs(a[i] - a[i-1]) for i in range(1, n))

