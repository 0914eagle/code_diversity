def x_or_y(n, x, y):
    
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return x_or_y(n // 2, x, y)
    else:
        return x_or_y(n // 2, y, x)


