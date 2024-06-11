def digits(n):
    
    if n < 10 and n % 2 == 1:
        return n
    elif n < 10:
        return 0
    else:
        return digits(n // 10) * (n % 10 if n % 2 != 0 else 1)


