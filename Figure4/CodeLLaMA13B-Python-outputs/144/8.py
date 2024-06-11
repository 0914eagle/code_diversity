def simplify(x, n):
    
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    x_num, x_den = int(x_num), int(x_den)
    n_num, n_den = int(n_num), int(n_den)
    return (x_num * n_den) % x_den == 0 and (n_num * x_den) % n_den == 0
