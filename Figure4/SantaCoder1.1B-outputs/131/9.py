def digits(n):
    
    if n == 0:
        return 0
    else:
        return n * digits(n % 10)


