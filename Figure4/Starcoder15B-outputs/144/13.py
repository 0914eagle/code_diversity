def simplify(x, n):
    
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")

    x_num = int(x_num)
    x_den = int(x_den)
    n_num = int(n_num)
    n_den = int(n_den)

    if x_den == n_den:
        return (x_num * n_num) % x_den == 0
    else:
        return False


