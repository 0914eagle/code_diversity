def is_simple_power(x, n):
    
    if n == 1:
        return True
    if n % x != 0:
        return False
    return is_simple_power(n // x, x)


