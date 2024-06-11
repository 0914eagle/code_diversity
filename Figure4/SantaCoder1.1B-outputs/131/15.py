def digits(n):
    
    if n == 0:
        return 0
    if n < 10:
        return n
    result = 1
    while n > 0:
        result *= n % 10
        n //= 10
    return result


