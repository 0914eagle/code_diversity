def digits(n):
    
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod


