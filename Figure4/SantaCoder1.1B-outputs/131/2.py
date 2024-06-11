def digits(n):
    
    if n < 10:
        return n
    return sum(int(d) for d in str(n))


