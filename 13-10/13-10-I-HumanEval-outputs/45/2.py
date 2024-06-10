
def simplify(x: str, n: str) -> bool:
    

    # convert the strings to integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # multiply the two fractions
    prod_num = x_num * n_num
    prod_denom = x_denom * n_denom

    # check if the product is a whole number
    if prod_num % prod_denom == 0:
        return True
    else:
        return False

