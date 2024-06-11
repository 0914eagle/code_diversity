def simplify(x, n):
    
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    if x_den == n_num:
        return True
    return False


