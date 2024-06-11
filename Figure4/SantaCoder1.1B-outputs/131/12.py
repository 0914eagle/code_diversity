def digits(n):
    
    if n < 10:
        return n
    else:
        return n % 10 * digits(n // 10)


