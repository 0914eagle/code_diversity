def make_a_pile(n):
    
    if n % 2 == 0:
        return [n, n+1, n+2]
    else:
        return [n, n+1]


