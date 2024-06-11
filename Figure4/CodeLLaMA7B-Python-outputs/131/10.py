def digits(n):
    
    if n == 0:
        return 0
    else:
        product = 1
        while n > 0:
            if n % 2 != 0:
                product *= (n % 10)
            n = n // 10
        return product


