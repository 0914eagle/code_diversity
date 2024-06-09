
def solve(A, B, n, x):
    result = x
    for i in range(n):
        result = (A * result + B) % 1000000007
    return result

