
def simplify(x: str, n: str) -> bool:
    
    num1, denom1 = x.split('/')
    num2, denom2 = n.split('/')
    product = int(num1) * int(num2)
    denominator = int(denom1) * int(denom2)
    return product % denominator == 0

