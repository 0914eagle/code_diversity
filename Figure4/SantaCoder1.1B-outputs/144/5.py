def simplify(x, n):
    
    x = x.split("/")
    x = [int(i) for i in x]
    n = int(n)
    if x[0] * n == x[1]:
        return True
    else:
        return False


