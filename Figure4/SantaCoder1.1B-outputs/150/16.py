def x_or_y(n, x, y):
    
    if n < 1:
        return None
    if n == 1:
        return x
    if n % 2 == 0:
        return x_or_y(n // 2, x, y)
    else:
        return y

