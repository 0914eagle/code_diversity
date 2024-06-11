def digits(n):
    
    product = 1
    for i in str(n):
        if int(i) % 2 != 0:
            product *= int(i)
    return product


