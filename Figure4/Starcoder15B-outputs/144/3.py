def simplify(x, n):
    
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")
    return (int(x_numerator) * int(n_numerator)) % (int(x_denominator) * int(n_denominator)) == 0


