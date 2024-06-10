
def simplify(x: str, n: str) -> bool:
    
    numerator_x, denominator_x = x.split('/')
    numerator_n, denominator_n = n.split('/')
    product = int(numerator_x) * int(numerator_n) // int(denominator_x) * int(denominator_n)
    return product % 1 == 0

