
def f1(n, f):
    # Base case: if f is already idempotent, return 1
    if f == f(f(1)):
        return 1
    
    # Inductive step: try applying f twice and see if it's idempotent
    k = 2
    while f(f(k)) != f(k):
        k += 1
    
    return k

