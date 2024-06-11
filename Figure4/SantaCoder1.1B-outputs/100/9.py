def make_a_pile(n):
    
    if n % 2 == 0:
        return [n]
    else:
        return [n, n+1]


