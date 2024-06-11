def make_a_pile(n):
    
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n, n + 1]
    else:
        return [n, n + 1, n + 2]


