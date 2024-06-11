def make_a_pile(n):
    
    if n < 1:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1]
    if n % 2 == 0:
        return [n, n - 2] + make_a_pile(n - 2)
    else:
        return [n, n - 1] + make_a_pile(n - 1)


