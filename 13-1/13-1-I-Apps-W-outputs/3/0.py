
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f == f[0]:
        return 1
    
    # Initialize variables
    k = 1
    g = f
    
    # Iterate until g is idempotent
    while g != g[0]:
        g = [f[i-1] for i in g]
        k += 1
    
    return k

