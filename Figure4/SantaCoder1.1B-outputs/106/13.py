def f(n):
    
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [n * f(n - 1) for n in range(1, n + 1)]


