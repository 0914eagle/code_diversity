
def simplify(x: str, n: str) -> bool:
    
    # Convert the strings to integers
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Multiply the fractions
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # Check if the product is a whole number
    if product_num % product_denom == 0:
        return True
    else:
        return False

