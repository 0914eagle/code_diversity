def digits(n):
    
    if n < 10:
        return n
    else:
        if n % 2 == 0:
            return digits(n // 10)
        else:
            return n % 10 * digits(n // 10)


