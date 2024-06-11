def simplify(x, n):
    
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')

    x_num = int(x_num)
    x_den = int(x_den)
    n_num = int(n_num)
    n_den = int(n_den)

    return (x_num * n_den) % n_num == 0


# Tests
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
