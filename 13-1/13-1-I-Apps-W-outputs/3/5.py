
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f == f(f(1)):
        return 1
    
    # Initialize variables
    k = 2
    g = f
    
    # Iterate until g is idempotent
    while g != g(g(1)):
        g = f(g(1))
        k += 1
    
    return k

