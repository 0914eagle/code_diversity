def simplify(x, n):
    
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    return (int(x_numerator) * int(n_denominator)) % int(x_denominator) == 0


if __name__ == '__main__':
    print(simplify("1/5", "5/1"))
    print(simplify("1/6", "2/1"))
    print(simplify("7/10", "10/2"))
