def x_or_y(n, x, y):
    
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return x_or_y(n // 2, x, y)
    else:
        return x_or_y(n // 2, y, x)


