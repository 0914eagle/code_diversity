def is_simple_power(x, n):
    
    if n == 1:
        return True
    if x == n:
        return True
    if x % n == 0:
        return is_simple_power(x / n, n)
    return False


