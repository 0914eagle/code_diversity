def digits(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return sum(int(d) for d in str(n))


