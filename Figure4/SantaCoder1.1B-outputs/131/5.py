def digits(n):
    
    if n == 0:
        return 0
    else:
        return sum(int(d) for d in str(n))


