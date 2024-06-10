
def simplify(x: str, n: str) -> bool:
    
    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')

    product_num = int(x_num) * int(n_num)
    product_denom = int(x_denom) * int(n_denom)

    return product_num % product_denom == 0

