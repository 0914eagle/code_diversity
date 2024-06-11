def digits(n):
    
    if n < 10:
        return n
    else:
        return digits(n // 10) * 10 + n % 10

