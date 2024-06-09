
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f(f(1)) == f(1):
        return 1
    
    # Inductive step: try applying f twice and check if it is idempotent
    k = 2
    while f(f(f(1))) != f(f(1)):
        k += 1
        if k > n:
            return -1
    
    return k

