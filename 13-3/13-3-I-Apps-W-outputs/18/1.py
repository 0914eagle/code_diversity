
def g_n(A, B, n, x):
    if n == 0:
        return x
    else:
        return (A * g_n(A, B, n-1, x) + B) % 1000000007

