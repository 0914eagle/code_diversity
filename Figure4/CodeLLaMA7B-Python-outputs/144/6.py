def simplify(x, n):
    
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    return (int(x_numerator) * int(n_denominator)) % int(x_denominator) == 0


# tests
