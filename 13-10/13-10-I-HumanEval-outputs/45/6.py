
def simplify(x: str, n: str) -> bool:
    
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')
    product_numerator = int(x_numerator) * int(n_numerator)
    product_denominator = int(x_denominator) * int(n_denominator)
    return product_numerator % product_denominator == 0

