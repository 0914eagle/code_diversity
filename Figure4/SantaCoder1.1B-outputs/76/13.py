def is_simple_power(x, n):
    
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_simple_power(x, n // 2)
    else:
        return x % n == 0

