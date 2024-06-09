
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f(f(1)) == f(1):
        return 1
    
    # Inductive step: try applying f twice and see if it's idempotent
    k = 2
    while k <= n:
        if f(f(f(1))) == f(f(1)):
            return k
        k += 1
    
    # If we reach this point, f is not idempotent
    return -1

