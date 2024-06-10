
def simplify(x: str, n: str) -> bool:
    
    numerator_x, denominator_x = x.split('/')
    numerator_n, denominator_n = n.split('/')

    product_numerator = int(numerator_x) * int(numerator_n)
    product_denominator = int(denominator_x) * int(denominator_n)

    if product_numerator % product_denominator == 0:
        return True
    else:
        return False

