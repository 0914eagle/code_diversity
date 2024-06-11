def simplify(x, n):
    
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    return (int(x_num) * int(n_den) * int(n_num) * int(x_den)) % (int(x_den) * int(n_den)) == 0


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
