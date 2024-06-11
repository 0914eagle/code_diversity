def simplify(x, n):
    
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)
    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)

    if x_denominator == n_denominator:
        return x_numerator % n_numerator == 0
    else:
        return (x_numerator * n_denominator) % (x_denominator * n_numerator) == 0


print(simplify("1/5", "5/1"))
print(simplify("1/6", "2/1"))
print(simplify("7/10", "10/2"))
