def make_a_pile(n):
    
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + make_a_pile(n - 1)
    else:
        return [n] + make_a_pile(n - 2)


