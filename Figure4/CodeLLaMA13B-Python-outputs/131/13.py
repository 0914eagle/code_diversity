def digits(n):
    
    if n < 10:
        return n
    if n % 2 == 0:
        return 0
    return n % 10 * digits(n // 10)


