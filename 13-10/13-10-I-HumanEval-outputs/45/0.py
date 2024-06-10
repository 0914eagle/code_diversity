
def simplify(x: str, n: str) -> bool:
    

    # convert the input strings to integers
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))

    # simplify the fractions
    product = num1 * num2 / (denom1 * denom2)

    # check if the product is a whole number
    return product % 1 == 0

