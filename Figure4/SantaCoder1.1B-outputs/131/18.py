def digits(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 10 == 0:
        return 0
    return n % 10 * digits(n // 10)


