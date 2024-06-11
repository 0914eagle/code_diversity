def digits(n):
    
    if n < 10 and n % 2 == 1:
        return n
    if n < 10:
        return 0
    if n % 2 == 0:
        return digits(int(n / 10))
    return n % 10 * digits(int(n / 10))


