def digits(n):
    
    odd_digits = [int(x) for x in str(n) if int(x) % 2 != 0]
    return reduce(lambda x, y: x * y, odd_digits, 1)


