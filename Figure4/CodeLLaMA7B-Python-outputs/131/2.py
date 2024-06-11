def digits(n):
    
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    else:
        return n % 10 * digits(n // 10)


