def simplify(x, n):
    
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    if int(x_den) % int(n_den) == 0:
        return True
    return False

