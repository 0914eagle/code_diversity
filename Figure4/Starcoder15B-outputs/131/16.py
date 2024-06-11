def digits(n):
    
    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 != 0]
    if len(odd_digits) == 0:
        return 0
    else:
        return reduce(lambda x, y: x * y, odd_digits)

