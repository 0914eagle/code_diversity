def simplify(x, n):
    
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")
    x_numerator, x_denominator = int(x_numerator), int(x_denominator)
    n_numerator, n_denominator = int(n_numerator), int(n_denominator)
    return (x_numerator * n_denominator) % n_numerator == 0 and (n_numerator * x_denominator) % x_numerator == 0


