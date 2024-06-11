def digits(n):
    
    if n == 0:
        return 0
    return sum(d for d in str(n) if d % 2 == 1)


