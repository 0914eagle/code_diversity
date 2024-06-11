def make_a_pile(n):
    
    if n % 2 == 0:
        return [n] + make_a_pile(n // 2)
    else:
        return [n] + make_a_pile(n // 2 + 1)


