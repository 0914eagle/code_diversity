
def polynomial_plotter(n, a):
    # Initialize the constants
    C = [0] * (n+1)
    C[0] = a[0]
    for i in range(1, n+1):
        C[i] = C[i-1] + a[i]
    return C

