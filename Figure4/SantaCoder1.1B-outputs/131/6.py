def digits(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n % 10) * digits(n // 10)

