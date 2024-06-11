def make_a_pile(n):
    
    if n % 2 == 0:
        return [n // 2]
    else:
        return [n // 2, n + 1]


