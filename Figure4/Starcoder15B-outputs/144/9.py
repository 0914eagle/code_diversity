def simplify(x, n):
    
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    return int(x_num) * int(n_num) % int(x_den) == 0 and int(x_num) * int(n_num) % int(n_den) == 0


