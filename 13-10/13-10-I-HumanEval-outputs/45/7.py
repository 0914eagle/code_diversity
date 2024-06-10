
def simplify(x: str, n: str) -> bool:
    
    # Convert the strings to integers
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Multiply the fractions
    prod_num = x_num * n_num
    prod_den = x_den * n_den

    # Check if the result is a whole number
    return prod_num % prod_den == 0

