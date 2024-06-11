def x_or_y(n, x, y):
    
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return x_or_y(n // 2, x, y)
    else:
        return x_or_y(n // 2, y, x)


