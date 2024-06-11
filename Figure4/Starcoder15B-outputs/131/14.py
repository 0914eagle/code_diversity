def digits(n):
    
    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 != 0]
    if odd_digits:
        return reduce(lambda x, y: x * y, odd_digits)
    else:
        return 0


