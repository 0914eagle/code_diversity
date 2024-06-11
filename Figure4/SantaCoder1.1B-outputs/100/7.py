def make_a_pile(n):
    
    if n == 1:
        return [n]
    if n % 2 == 0:
        return [n, n + 1]
    else:
        return [n + 1, n]


