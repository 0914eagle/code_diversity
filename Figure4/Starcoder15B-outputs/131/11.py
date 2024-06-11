def digits(n):
    
    odds = [int(x) for x in str(n) if int(x) % 2 != 0]
    return reduce(lambda x, y: x * y, odds, 1)

